#!/usr/bin/env python3
"""Package sanitized Landing design artifacts with a verified manifest."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import tempfile


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
            raise SystemExit(f"Symlinked output path is not allowed: {current}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source_dir", type=Path)
    parser.add_argument("portable_dir", type=Path)
    parser.add_argument("--packet-id", required=True)
    parser.add_argument("--source-release", required=True)
    args = parser.parse_args()
    if not PACKET_ID.fullmatch(args.packet_id):
        raise SystemExit("Invalid packet ID")
    source_input = args.source_dir.expanduser().absolute()
    destination_input = args.portable_dir.expanduser().absolute()
    if source_input.is_symlink():
        raise SystemExit("Source symlinks are not allowed")
    source = source_input.resolve()
    if not source.is_dir():
        raise SystemExit("Source must be a real directory")
    if tuple(part.casefold() for part in destination_input.parts[-3:]) != ("deliverables", "design-kit", "portable"):
        raise SystemExit("Destination must be <landing-root>/deliverables/design-kit/portable")
    module_root_input = destination_input.parents[2]
    if module_root_input.is_symlink():
        raise SystemExit("Symlinked module root is not allowed")
    reject_symlink_components(module_root_input, destination_input)
    module_root = module_root_input.resolve()
    destination = destination_input.resolve(strict=False)
    if not inside(module_root, destination):
        raise SystemExit("Destination escapes landing root")

    files: list[tuple[Path, str]] = []
    for path in sorted(source.rglob("*")):
        if path.is_symlink():
            raise SystemExit(f"Symlinks are not allowed: {path}")
        if path.is_file():
            if not inside(source, path.resolve()):
                raise SystemExit(f"Path escapes source: {path}")
            relative = path.relative_to(source).as_posix()
            if relative == "manifest.json":
                raise SystemExit("Source must not contain manifest.json")
            files.append((path, relative))
    if not files:
        raise SystemExit("Source has no files")

    destination.parent.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix=".design-kit-", dir=destination.parent))
    try:
        entries = []
        for path, relative in files:
            target = staging / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, target)
            entries.append({"path": relative, "sha256": digest(target), "role": Path(relative).stem.replace("_", "-")})
        manifest = {
            "schema": "premium-landing.design-kit.v1",
            "packet_id": args.packet_id,
            "created_at": datetime.now(timezone.utc).isoformat(),
            "source_release": args.source_release,
            "files": entries,
        }
        (staging / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
        if destination.exists():
            if destination.is_symlink() or not destination.is_dir() or any(destination.iterdir()):
                raise SystemExit(f"Destination already exists and is not empty: {destination}")
            destination.rmdir()
        staging.replace(destination)
    except Exception:
        shutil.rmtree(staging, ignore_errors=True)
        raise
    print(f"Packet: {args.packet_id}")
    print(f"Manifest SHA-256: {digest(destination / 'manifest.json')}")
    print(f"Destination: {destination}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
