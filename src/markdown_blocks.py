import re
from enum import Enum


class BlockType(Enum):
    PARAGRAPH = 1,
    HEADING = 2,
    CODE = 3,
    QUOTE = 4,
    UNORDERED_LIST = 5,
    ORDERED_LIST = 6,


def markdown_to_blocks(markdown):
    blocks = markdown.split('\n\n')

    block_list = []
    for block in blocks:
        if block.strip():
            block_list.append(block.strip())

    return block_list


def block_to_block_type(markdown_block):
    if re.search("^#{1,6} ", markdown_block):
        return BlockType.HEADING
    if markdown_block.startswith("```") and markdown_block.endswith("```"):
        return BlockType.CODE
    if re.search("^> ?", markdown_block):
        return BlockType.QUOTE
    if re.search("^- ", markdown_block):
        return BlockType.UNORDERED_LIST
    if re.search(r"^\d{1,}\. ", markdown_block):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH
