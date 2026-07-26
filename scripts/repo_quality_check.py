from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEXT_SUFFIXES = {".md", ".py", ".json", ".yml", ".yaml"}
V2_ROOTS = [
    "11-v2-foundation",
    "12-research",
    "13-system",
    "14-method-validation",
    "15-implementation",
    "16-operational-playbooks",
]
EXEMPT_MARKDOWN = {"README.md", "CONTRIBUTING.md"}


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def text_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*")
        if path.is_file()
        and ".git" not in path.parts
        and "__pycache__" not in path.parts
        and path.suffix.lower() in TEXT_SUFFIXES
    )


def read_utf8(path: Path, errors: list[str]) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        fail(errors, f"UTF-8 decode failed: {path.relative_to(ROOT)}: {exc}")
        return ""


def check_json(path: Path, text: str, errors: list[str]) -> None:
    try:
        json.loads(text)
    except Exception as exc:  # noqa: BLE001 - quality gate must report parser details
        fail(errors, f"invalid JSON: {path.relative_to(ROOT)}: {exc}")


def check_document_id(
    path: Path,
    text: str,
    document_ids: dict[str, Path],
    errors: list[str],
) -> None:
    if path.name in EXEMPT_MARKDOWN:
        return
    match = re.search(r"^document_id:\s*(\S+)\s*$", text, re.MULTILINE)
    if not match:
        fail(errors, f"missing document_id: {path.relative_to(ROOT)}")
        return
    document_id = match.group(1)
    previous = document_ids.get(document_id)
    if previous is not None:
        fail(
            errors,
            "duplicate document_id "
            f"{document_id}: {previous.relative_to(ROOT)} and {path.relative_to(ROOT)}",
        )
        return
    document_ids[document_id] = path


def check_readme(errors: list[str]) -> None:
    readme = ROOT / "README.md"
    if not readme.is_file():
        fail(errors, "README.md is missing")
        return
    text = read_utf8(readme, errors)
    if "v2.0.0" not in text:
        fail(errors, "README.md does not identify v2.0.0 as the current controlled version")
    required_links = [
        "12-research/01-cma-one-list-one-library-dossier.md",
        "13-system/02-evidence-object-and-manifest-model.md",
        "14-method-validation/01-general-method-validation-master-plan.md",
        "15-implementation/01-24-month-integrated-roadmap.md",
        "16-operational-playbooks/02-acquisition-session-playbook.md",
    ]
    for rel in required_links:
        if rel not in text:
            fail(errors, f"README.md is missing navigation link: {rel}")
        if not (ROOT / rel).is_file():
            fail(errors, f"README.md links to missing file: {rel}")


def check_v2(errors: list[str]) -> tuple[int, int]:
    files: list[Path] = []
    for rel in V2_ROOTS:
        directory = ROOT / rel
        if not directory.is_dir():
            fail(errors, f"missing v2 directory: {rel}")
            continue
        files.extend(sorted(path for path in directory.rglob("*.md") if path.is_file()))
    line_count = sum(
        len(read_utf8(path, errors).splitlines())
        for path in files
    )
    if len(files) < 35:
        fail(errors, f"v2 controlled documents {len(files)} < 35")
    if line_count < 22000:
        fail(errors, f"v2 controlled-document lines {line_count} < 22000")
    return len(files), line_count


def check_one_time_material(errors: list[str]) -> None:
    for rel in ("bootstrap", "bootstrap-v2"):
        if (ROOT / rel).exists():
            fail(errors, f"one-time material still exists: {rel}")
    for rel in (
        ".github/workflows/bootstrap-docs.yml",
        ".github/workflows/v2-materialize.yml",
    ):
        if (ROOT / rel).exists():
            fail(errors, f"one-time workflow still exists: {rel}")
    permanent = ROOT / ".github/workflows/documentation-quality.yml"
    if not permanent.is_file():
        fail(errors, "permanent documentation-quality workflow is missing")


def main() -> int:
    errors: list[str] = []
    files = text_files()
    document_ids: dict[str, Path] = {}
    total_lines = 0

    for path in files:
        text = read_utf8(path, errors)
        total_lines += len(text.splitlines())
        suffix = path.suffix.lower()
        if suffix == ".json":
            check_json(path, text, errors)
        if suffix == ".md":
            check_document_id(path, text, document_ids, errors)

    if len(files) < 20:
        fail(errors, f"text files {len(files)} < 20")
    if total_lines < 8000:
        fail(errors, f"total text lines {total_lines} < 8000")
    if len(document_ids) < 90:
        fail(errors, f"controlled document IDs {len(document_ids)} < 90")

    check_readme(errors)
    v2_files, v2_lines = check_v2(errors)
    check_one_time_material(errors)

    print(f"Text files: {len(files)}")
    print(f"Total text lines: {total_lines}")
    print(f"Controlled document IDs: {len(document_ids)}")
    print(f"v2 controlled documents: {v2_files}")
    print(f"v2 controlled-document lines: {v2_lines}")

    if errors:
        print("QUALITY GATE FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("QUALITY GATE PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
