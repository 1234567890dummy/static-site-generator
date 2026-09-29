import re

from textnode import TextNode, TextType


def split_nodes_delimiter(
    old_nodes: list[TextNode],
    delimiter: str,
    text_type: TextType) -> list[TextNode]:

    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_old_node = old_node.text.split(delimiter)
        for index in range(len(split_old_node)):
            if len(split_old_node) % 2 == 0:
                raise Exception(f"missing closing delimiter {delimiter}")
            if index % 2 == 0:
                new_nodes.append(TextNode(split_old_node[index], TextType.TEXT))
            else:
                new_nodes.append(TextNode(split_old_node[index], text_type))

    return new_nodes


def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches


def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        remaining_text = old_node.text
        extracted = extract_markdown_images(remaining_text)
        if not extracted:
            new_nodes.append(old_node)
            continue
        for extract in extracted:
            image_alt, image_link = extract
            sections = remaining_text.split(f"![{image_alt}]({image_link})", 1)
            if sections[0]:
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
            remaining_text = sections[1]
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))

    return new_nodes


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        remaining_text = old_node.text
        extracted = extract_markdown_links(remaining_text)
        if not extracted:
            new_nodes.append(old_node)
            continue
        for extract in extracted:
            label, url = extract
            sections = remaining_text.split(f"[{label}]({url})", 1)
            if sections[0]:
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(label, TextType.LINK, url))
            remaining_text = sections[1]
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))

    return new_nodes


def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, '**', TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, '_', TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, '`', TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    return nodes
