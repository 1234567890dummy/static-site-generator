from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, props)

    def to_html(self):
        if not self.value:
            raise ValueError
        if not self.tag:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f'\nLeafNode: (tag) {self.tag} \n\t(value) {self.value} \n\t(props) {self.props}'
