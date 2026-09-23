from htmlnode import HTMLNode
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    def to_html(self):
        if self.tag is None:
            raise ValueError("Missing tag")
        if self.children is None:
            raise ValueError("Missing children")
        children_html = ""
        for child in self.children:
             children_html += child.to_html()
        return f"<{self.tag if self.props is None else self.tag + " "}{self.props_to_html()}>{children_html}</{self.tag}>"
