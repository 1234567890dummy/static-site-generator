import shutil
from pathlib import Path
from sys import argv

from generate_page import generate_page_recursive

PROJECT_ROOT = Path(__file__).resolve().parent.parent
STATIC_DIR = PROJECT_ROOT / "static"
DOCS_DIR = PROJECT_ROOT / "docs"

def main():
    if len(argv) > 1:
        basepath = argv[1]
    else:
        basepath = "/"

    public_flush()
    static_to_public(STATIC_DIR, DOCS_DIR)
    generate_page_recursive(
        PROJECT_ROOT / "content",
        PROJECT_ROOT / "template.html",
        DOCS_DIR,
        basepath
    )

def public_flush():
    if DOCS_DIR.exists():
        shutil.rmtree(DOCS_DIR)
    DOCS_DIR.mkdir()

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
