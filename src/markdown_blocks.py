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
    split_markdown = markdown.split('\n\n')
    split_markdown.strip()
    for index, val in enumerate(split_markdown):
        if not val:
            split_markdown.pop(index)

    return split_markdown


def block_to_block_type(markdown_block):
    if re.search("/^#{1,6} ./", markdown_block):
        return BlockType.HEADING
    if re.search("/^`{3}\n`{3}$/", markdown_block):
        return BlockType.CODE
    if re.search("/^> ?/", markdown_block):
        return BlockType.QUOTE
    if re.search("/^- /", markdown_block):
        return BlockType.UNORDERED_LIST
    if re.search("/^\d\. /", markdown_block):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH
