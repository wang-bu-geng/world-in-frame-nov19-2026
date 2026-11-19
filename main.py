import os
from pathlib import Path
from shutil import copyfile

def main():
    image = Path(__file__).resolve().with_name("entry.png")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    copyfile(image, output_dir / "entry.png")


if __name__ == "__main__":
    main()
