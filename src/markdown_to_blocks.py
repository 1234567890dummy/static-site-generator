def markdown_to_blocks(markdown):
    split_markdown = markdown.split('\n\n')
    split_markdown.strip()
    for index, val in enumerate(split_markdown):
        if not val:
            split_markdown.pop(index)
