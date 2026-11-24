"""Copy entry.png to the output directory.

The entry image is rendered by render.py and stored in this repository
as entry.png. This program copies it, byte for byte, to
/output/entry.png (or $MAKEFUN_OUTPUT_DIR/entry.png), deterministically.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"


def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / "entry.png"
    if not SRC.is_file():
        raise SystemExit(f"entry.png not found next to {__file__}")
    shutil.copyfile(SRC, dest)


if __name__ == "__main__":
    main()
