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
                new_nodes.append(TextNode(split_old_node[i], TextType.TEXT))
            else:
                new_nodes.append(TextNode(split_old_node[i], text_type))

    return new_nodes
