"""Prepare local release assets from an existing tag without publishing anything."""

import argparse
from datetime import date
import hashlib
from pathlib import Path
import re
import subprocess
import sys


NUMBER = r"(?:0|[1-9][0-9]*)"
PRERELEASE_ID = rf"(?:{NUMBER}|[0-9A-Za-z-]*[A-Za-z-][0-9A-Za-z-]*)"
TAG_PATTERN = re.compile(
    rf"v(?P<version>{NUMBER}\.{NUMBER}\.{NUMBER}"
    rf"(?:-(?P<prerelease>{PRERELEASE_ID}(?:\.{PRERELEASE_ID})*))?)"
)


def release_version(tag: str) -> str:
    match = TAG_PATTERN.fullmatch(tag)
    if match is None:
        raise ValueError("Use vMAJOR.MINOR.PATCH with an optional SemVer prerelease suffix.")
    return match.group("version")


def release_notes(changelog: str, version: str) -> str:
    headings = list(re.finditer(r"^## .*?$", changelog, re.MULTILINE))
    candidates = []
    for index, heading in enumerate(headings):
        match = re.fullmatch(r"## \[([^\]]+)\] - (\d{4}-\d{2}-\d{2})[ \t]*", heading.group())
        if match and match.group(1) == version:
            date.fromisoformat(match.group(2))
            end = headings[index + 1].start() if index + 1 < len(headings) else len(changelog)
            candidates.append(changelog[heading.end():end].strip())
    if len(candidates) != 1:
        raise ValueError(f"CHANGELOG.md needs exactly one dated entry for [{version}].")
    body = candidates[0]
    for section in ("Compatibility", "Migration"):
        match = re.search(
            rf"^### {section}[ \t]*\n(?P<body>.*?)(?=^### |\Z)",
            body,
            re.MULTILINE | re.DOTALL,
        )
        if match is None or not match.group("body").strip():
            raise ValueError(f"The release entry needs a substantive {section} section.")
    return body


def git_text(repo: Path, *args: str) -> str:
    return subprocess.check_output(
        ["git", "-C", str(repo), *args], encoding="utf-8", stderr=subprocess.PIPE
    ).strip()


def prepare_release(repo: Path, tag: str, output_dir: Path) -> tuple[Path, Path, Path]:
    version = release_version(tag)
    commit = git_text(repo, "rev-parse", "--verify", f"refs/tags/{tag}^{{commit}}")
    if git_text(repo, "rev-parse", "HEAD") != commit:
        raise ValueError("Check out the tagged commit before preparing its release.")
    changelog = git_text(repo, "show", f"{commit}:CHANGELOG.md")
    notes = release_notes(changelog, version)

    output_dir.mkdir(parents=True, exist_ok=True)
    name = f"product-foundation-kit-{tag}"
    archive = output_dir / f"{name}.zip"
    subprocess.run(
        [
            "git", "-C", str(repo), "archive", "--format=zip",
            f"--prefix={name}/", "--output", str(archive.resolve()), commit,
        ],
        check=True,
        stderr=subprocess.PIPE,
    )
    checksum = archive.with_suffix(".zip.sha256")
    checksum.write_text(
        f"{hashlib.sha256(archive.read_bytes()).hexdigest()}  {archive.name}\n",
        encoding="utf-8",
    )
    notes_path = output_dir / "release-notes.md"
    notes_path.write_text(
        f"# Product Foundation Kit {tag}\n\n"
        f"Source commit: `{commit}`\n\n{notes}\n",
        encoding="utf-8",
    )
    return archive, checksum, notes_path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tag", required=True)
    parser.add_argument("--output-dir", type=Path, default=Path("dist"))
    args = parser.parse_args()
    try:
        assets = prepare_release(Path.cwd(), args.tag, args.output_dir)
    except (ValueError, OSError, subprocess.CalledProcessError) as error:
        print(f"Release preparation failed: {error}", file=sys.stderr)
        if isinstance(error, subprocess.CalledProcessError) and error.stderr:
            detail = error.stderr
            print(detail.decode("utf-8", errors="replace") if isinstance(detail, bytes) else detail, file=sys.stderr)
        return 1
    for asset in assets:
        print(asset)
    return 0


if __name__ == "__main__":
    sys.exit(main())
