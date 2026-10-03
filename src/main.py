import shutil
from pathlib import Path

from generate_page import generate_page

PROJECT_ROOT = Path(__file__).resolve().parent.parent
STATIC_DIR = PROJECT_ROOT / "static"
PUBLIC_DIR = PROJECT_ROOT / "public"

def main():
    public_flush()
    static_to_public(STATIC_DIR, PUBLIC_DIR)
    generate_page(
        PROJECT_ROOT / "content" / "index.md",
        PROJECT_ROOT / "template.html",
        PUBLIC_DIR / "index.html",
    )

def public_flush():
    if PUBLIC_DIR.exists():
        shutil.rmtree(PUBLIC_DIR)
    PUBLIC_DIR.mkdir()

def static_to_public(src, dst):
    for item in src.iterdir():
        target = dst / item.name
        if item.is_file():
            shutil.copy(item, target)
        else:
            target.mkdir(exist_ok=True)
            static_to_public(item, target)


if __name__ == "__main__":
    main()
