
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
