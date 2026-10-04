"""Release-tooling checks; these do not lint or certify kit documentation."""

import hashlib
import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import zipfile


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "prepare_release.py"
SPEC = importlib.util.spec_from_file_location("prepare_release", SCRIPT)
release = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(release)


def changelog(version="1.2.3", release_date="2026-10-04"):
    return (
        "# Changelog\n\n## [Unreleased]\n\nFuture changes.\n\n"
        f"## [{version}] - {release_date}\n\n### Added\n\n- Fixture capability.\n\n"
        "### Compatibility\n\nExisting artifacts remain valid.\n\n"
        "### Migration\n\nNo conversion required.\n\n"
        "## [1.2.2] - 2026-09-01\n\nOlder changes.\n"
    )


class ReleaseMetadataTests(unittest.TestCase):
    def test_stable_and_prerelease_versions(self):
        for tag in ("v0.1.0", "v1.2.3", "v1.0.0-rc.1", "v1.0.0-0", "v1.0.0-alpha-01"):
            with self.subTest(tag=tag):
                self.assertEqual(release.release_version(tag), tag[1:])

    def test_invalid_tags(self):
        for tag in (
            "1.2.3", "v1", "v01.2.3", "v1.2.3-01", "v1.2.3-rc..1",
            "v1.2.3+build", "v1.2.3/extra", "v1.2.3\n", "v1.2.3;command",
        ):
            with self.subTest(tag=tag), self.assertRaises(ValueError):
                release.release_version(tag)

    def test_only_selected_release_notes_are_extracted(self):
        notes = release.release_notes(changelog(), "1.2.3")
        self.assertIn("Fixture capability", notes)
        self.assertNotIn("Future changes", notes)
        self.assertNotIn("Older changes", notes)

    def test_prerelease_notes(self):
        self.assertIn("Migration", release.release_notes(changelog("1.0.0-rc.1"), "1.0.0-rc.1"))

    def test_missing_and_duplicate_versions(self):
        for content in (changelog(), changelog() + changelog()):
            version = "9.0.0" if content == changelog() else "1.2.3"
            with self.subTest(version=version), self.assertRaises(ValueError):
                release.release_notes(content, version)

    def test_invalid_release_date(self):
        with self.assertRaises(ValueError):
            release.release_notes(changelog(release_date="2026-02-30"), "1.2.3")

    def test_missing_or_empty_compatibility_and_migration(self):
        for old, new in (
            ("### Compatibility", "### Other"),
            ("Existing artifacts remain valid.", ""),
            ("### Migration", "### Other"),
            ("No conversion required.", ""),
        ):
            with self.subTest(section=old), self.assertRaises(ValueError):
                release.release_notes(changelog().replace(old, new), "1.2.3")


class ReleasePackagingTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="kit-release-test-")
        self.addCleanup(self.temporary.cleanup)
        self.repo = Path(self.temporary.name) / "source"
        self.repo.mkdir()
        self.output = Path(self.temporary.name) / "output"
        self.git("init", "--quiet")
        self.git("config", "user.name", "Release tooling test")
        self.git("config", "user.email", "release-test@example.invalid")
        self.git("config", "commit.gpgsign", "false")
        self.git("config", "tag.gpgsign", "false")
        self.git("config", "core.autocrlf", "false")
        (self.repo / "CHANGELOG.md").write_text(changelog(), encoding="utf-8")
        (self.repo / "README.md").write_bytes(b"Tagged kit content.\n")
        (self.repo / "templates").mkdir()
        (self.repo / "templates" / "example.md").write_text("Canonical fixture.\n", encoding="utf-8")
        self.git("add", ".")
        self.git("commit", "--quiet", "-m", "Release fixture")
        self.git("tag", "-a", "v1.2.3", "-m", "Annotated fixture")
        self.commit = self.git("rev-parse", "HEAD")

    def git(self, *args):
        return subprocess.check_output(
            ["git", "-C", str(self.repo), *args], encoding="utf-8", stderr=subprocess.PIPE
        ).strip()

    def test_archive_uses_commit_and_checksum_matches_bytes(self):
        (self.repo / "README.md").write_text("Uncommitted change.", encoding="utf-8")
        (self.repo / "CHANGELOG.md").write_text("Uncommitted notes.", encoding="utf-8")
        (self.repo / "scratch.md").write_text("Untracked file.", encoding="utf-8")
        archive, checksum, notes = release.prepare_release(self.repo, "v1.2.3", self.output)
        with zipfile.ZipFile(archive) as package:
            prefix = "product-foundation-kit-v1.2.3/"
            self.assertEqual(package.read(prefix + "README.md"), b"Tagged kit content.\n")
            self.assertIn(prefix + "templates/example.md", package.namelist())
            self.assertFalse(any(".git/" in name or "scratch.md" in name for name in package.namelist()))
        self.assertEqual(
            checksum.read_text(encoding="utf-8"),
            f"{hashlib.sha256(archive.read_bytes()).hexdigest()}  {archive.name}\n",
        )
        self.assertIn(self.commit, notes.read_text(encoding="utf-8"))
        self.assertIn("Fixture capability", notes.read_text(encoding="utf-8"))

    def test_mismatched_checkout_does_not_create_assets(self):
        (self.repo / "later.md").write_text("Later commit.", encoding="utf-8")
        self.git("add", ".")
        self.git("commit", "--quiet", "-m", "Later fixture")
        with self.assertRaisesRegex(ValueError, "tagged commit"):
            release.prepare_release(self.repo, "v1.2.3", self.output)
        self.assertFalse(self.output.exists())

    def test_missing_tag_does_not_create_assets(self):
        with self.assertRaises(subprocess.CalledProcessError):
            release.prepare_release(self.repo, "v9.0.0", self.output)
        self.assertFalse(self.output.exists())

    def test_missing_release_entry_does_not_create_assets(self):
        self.git("tag", "v9.0.0")
        with self.assertRaisesRegex(ValueError, "dated entry"):
            release.prepare_release(self.repo, "v9.0.0", self.output)
        self.assertFalse(self.output.exists())

    def test_cli_success_and_failure(self):
        result = subprocess.run(
            [sys.executable, "-B", str(SCRIPT), "--tag", "v1.2.3", "--output-dir", str(self.output)],
            cwd=self.repo, capture_output=True, text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("release-notes.md", result.stdout)
        result = subprocess.run(
            [sys.executable, "-B", str(SCRIPT), "--tag", "v1.2.3-01"],
            cwd=self.repo, capture_output=True, text=True,
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn("Release preparation failed", result.stderr)
        self.assertFalse((self.repo / "dist").exists())


if __name__ == "__main__":
    unittest.main()
