import re
from pathlib import Path

from markdown_to_html import markdown_to_html_node


def extract_title(markdown):
    title = re.search(r"^# (.+)$", markdown, re.MULTILINE)
    if not title:
        raise Exception("ERROR: NO H1 HEADER FOUND")
    return title.group(1).strip()

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as file:
        from_path_file = file.read()
    with open(template_path, "r") as file:
        template_path_file = file.read()

    from_path_html_node = markdown_to_html_node(from_path_file)
    from_path_title = extract_title(from_path_file)
    new_html = template_path_file.replace("{{ Title }}", from_path_title)
    new_html = new_html.replace("{{ Content }}", from_path_html_node.to_html())

    # replace any instances of href="/ and src="/ with href="/{basepath} and src="/{basepath}
    new_html = new_html.replace('href="/', f'href="{basepath}')
    new_html = new_html.replace('src="/', f'src="{basepath}')

    Path(dest_path).parent.mkdir(parents=True, exist_ok=True)

    with open(dest_path, "w") as file:
        file.write(new_html)

def generate_page_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for item in dir_path_content.iterdir():
        target = dest_dir_path / item.name
        if item.is_file():
            if item.suffix == ".md":
                generate_page(item, template_path, target.with_suffix(".html"), basepath)
        else:
            generate_page_recursive(item, template_path, target, basepath)
