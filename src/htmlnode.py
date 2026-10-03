class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("child class must override")

    def props_to_html(self):
        return_string = f''
        if self.props:
            for prop in self.props:
                return_string += f' {prop}="{self.props[prop]}"'

        return return_string

    def __repr__(self):
        return f'\nHTMLNode: (tag) {self.tag} \n\t(value) {self.value} \n\t(children) {self.children} \n\t(props) {self.props}'


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")
        if not self.tag:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f'\nLeafNode: (tag) {self.tag} \n\t(value) {self.value} \n\t(props) {self.props}'


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

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
