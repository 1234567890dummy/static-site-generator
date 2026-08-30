from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("tag missing")
        if not self.children:
            raise ValueError("children missing")

        children_html = ""
        for child in self.children:
            children_html += child.to_html()

        o = f'<{self.tag}{self.props_to_html()}>'
        c = f'</{self.tag}>'

        return o + children_html + c
