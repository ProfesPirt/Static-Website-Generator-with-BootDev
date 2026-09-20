from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    def to_html(self):
        if not hasattr(self,"value"):
            raise ValueError
        if self.tag is None:
            return self.value
        return f"<{self.tag if self.props is None else self.tag + " "}{self.props_to_html()}>{self.value}</{self.tag}>"
    def __repr__(self):
        return f"Tag:{self.tag}, Value:{self.value}, Props:{self.props}"
