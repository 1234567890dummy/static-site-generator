from htmlnode import ParentNode
from inline_markdown import text_to_textnodes
from markdown_blocks import BlockType, block_to_block_type, markdown_to_blocks
from textnode import TextNode, TextType, text_node_to_html_node


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)

    children = []
    for block in blocks:
        children.append(block_to_html_node(block))

    return ParentNode(tag="div", children=children)


def block_to_html_node(block):
    block_type = block_to_block_type(block)

    if block_type == BlockType.HEADING:
        hashes = 0
        for char in block:
            if char == "#":
                hashes += 1
            else:
                break
        return ParentNode(tag=f"h{hashes}", children=text_to_children(block[hashes+1:].replace('\n',' ')))

    if block_type == BlockType.PARAGRAPH:
        split_block = block.splitlines()
        fixed_block = []
        for line in split_block:
            fixed_block.append(line.lstrip())
        fixed_block = ' '.join(fixed_block)
        return ParentNode(tag="p", children=text_to_children(fixed_block))

    if block_type == BlockType.CODE:
        split_block = block[4:-3].splitlines()
        fixed_block = []
        for line in split_block:
            fixed_block.append(line.lstrip())

        fixed_block = '\n'.join(fixed_block)
        inner = TextNode(text=fixed_block, text_type=TextType.CODE)
        inner = text_node_to_html_node(inner)
        return ParentNode(tag="pre", children=[inner])

    if block_type == BlockType.QUOTE:
        block_lines = block.splitlines()
        prepared_lines = []
        for block_line in block_lines:
            if block_line.startswith("> "):
                prepared_lines.append(block_line[2:])
            else:
                prepared_lines.append(block_line[1:])
        final_string = " ".join(prepared_lines)

        return ParentNode(tag="blockquote", children=text_to_children(final_string))

    if block_type == BlockType.ORDERED_LIST:
        block_lines = block.splitlines()
        prepared_lines = [block_line.split('.', 1)[1][1:] for block_line in block_lines]
        li_nodes = []
        for line in prepared_lines:
            li_nodes.append(ParentNode(tag="li", children=text_to_children(line)))

        return ParentNode(tag="ol", children=li_nodes)

    if block_type == BlockType.UNORDERED_LIST:
        block_lines = block.splitlines()
        prepared_lines = [block_line[2:] for block_line in block_lines]
        li_nodes = []
        for line in prepared_lines:
            li_nodes.append(ParentNode(tag="li", children=text_to_children(line)))

        return ParentNode(tag="ul", children=li_nodes)


def text_to_children(text):
    html_nodes = []
    text_nodes = text_to_textnodes(text)
    for text_node in text_nodes:
        html_nodes.append(text_node_to_html_node(text_node))

    return html_nodes
