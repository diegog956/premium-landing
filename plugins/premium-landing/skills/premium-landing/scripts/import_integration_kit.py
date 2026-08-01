#!/usr/bin/env python3
"""Validate and install a sibling Backoffice integration kit."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import tempfile


SCHEMA = "backoffice-builder.integration-kit.v1"
HASH = re.compile(r"[0-9a-f]{64}\Z")
PACKET_ID = re.compile(r"[a-z0-9][a-z0-9._-]{0,79}\Z")


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            value.update(chunk)
    return value.hexdigest()


def inside(root: Path, path: Path) -> bool:
    try:
        return os.path.normcase(os.path.commonpath((str(root), str(path)))) == os.path.normcase(str(root))
    except ValueError:
        return False


def reject_symlink_components(root: Path, path: Path) -> None:
    relative = path.relative_to(root)
    current = root
    for part in relative.parts:
        current = current / part
        if current.is_symlink():
            raise ValueError(f"Symlinked intake path is not allowed: {current}")


def load(manifest_path: Path) -> tuple[dict, list[tuple[Path, str]]]:
    if manifest_path.is_symlink() or not manifest_path.is_file():
        raise ValueError("Missing or unsafe manifest")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("schema") != SCHEMA:
        raise ValueError(f"Unsupported schema: {manifest.get('schema')!r}")
    packet_id = manifest.get("packet_id")
    if not isinstance(packet_id, str) or not PACKET_ID.fullmatch(packet_id):
        raise ValueError("Invalid packet_id")
    items = manifest.get("files")
    if not isinstance(items, list) or not items:
        raise ValueError("files must be non-empty")
    root = manifest_path.parent.resolve()
    verified: list[tuple[Path, str]] = []
    seen: set[str] = set()
    for index, item in enumerate(items):
        rel = item.get("path") if isinstance(item, dict) else None
        expected = item.get("sha256") if isinstance(item, dict) else None
        role = item.get("role") if isinstance(item, dict) else None
        if not isinstance(rel, str) or "\\" in rel or not isinstance(role, str) or not role:
            raise ValueError(f"File {index}: invalid path or role")
        pure = PurePosixPath(rel)
        if pure.is_absolute() or not pure.parts or any(part in ("", ".", "..") for part in pure.parts):
            raise ValueError(f"File {index}: unsafe path")
        normalized = pure.as_posix()
        if normalized == "manifest.json" or normalized in seen or not isinstance(expected, str) or not HASH.fullmatch(expected):
            raise ValueError(f"File {index}: duplicate, reserved, or invalid hash")
        path = root.joinpath(*pure.parts)
        if path.is_symlink() or not path.is_file() or not inside(root, path.resolve()) or digest(path) != expected:
            raise ValueError(f"File {index}: missing, escaped, or hash mismatch")
        seen.add(normalized)
        verified.append((path, normalized))
    return manifest, verified


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("overall_project_root", type=Path)
    parser.add_argument("landing_root", type=Path)
    args = parser.parse_args()
    overall = args.overall_project_root.expanduser().resolve()
    landing = args.landing_root.expanduser().resolve()
    source_manifest = overall / "backoffice" / "deliverables" / "integration-kit" / "portable" / "manifest.json"
    if not source_manifest.exists():
        print("No Backoffice integration kit found")
        return 0
    if landing != (overall / "landing").resolve() and not (landing / ".premium-landing").is_dir():
        raise SystemExit("Landing root must belong to the overall project")
    manifest, files = load(source_manifest)
    packet_id = manifest["packet_id"]
    intake = landing / "_inputs" / "integration-kit"
    reject_symlink_components(landing, intake)
    if not inside(landing, intake.resolve(strict=False)):
        raise SystemExit(f"Intake escapes landing root: {intake}")
    intake.mkdir(parents=True, exist_ok=True)
    destination = intake / packet_id
    if destination.is_symlink():
        raise SystemExit(f"Symlinked destination is not allowed: {destination}")
    if destination.exists():
        target_manifest = destination / "manifest.json"
        if target_manifest.is_symlink() or not target_manifest.is_file() or digest(source_manifest) != digest(target_manifest):
            raise SystemExit(f"Destination collision: {destination}")
    else:
        staging = Path(tempfile.mkdtemp(prefix=".integration-kit-", dir=intake))
        try:
            shutil.copy2(source_manifest, staging / "manifest.json")
            for source, relative in files:
                target = staging / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source, target)
            staging.replace(destination)
        except Exception:
            shutil.rmtree(staging, ignore_errors=True)
            raise
    current = {
        "packet_id": packet_id,
        "manifest_sha256": digest(source_manifest),
        "source": source_manifest.relative_to(overall).as_posix(),
    }
    temporary = intake / ".current.json.tmp"
    temporary.write_text(json.dumps(current, indent=2) + "\n", encoding="utf-8")
    temporary.replace(intake / "current.json")
    print(f"Installed packet: {packet_id}")
    print(f"Destination: {destination}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
