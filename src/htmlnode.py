
class HTMLNode():
    def __init__(self, tag=None , value=None , children=None , props=None ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplementedError()
    def props_to_html(self):
        return_string = ""
        if self.props is None:
            return return_string
        for prop in self.props:
            return_string += f'{prop}="{self.props[prop]}" '
        return return_string
    def __repr__(self):
        return f"Tag:{self.tag}, Value:{self.value}, Children:{self.children}, Props:{self.props}"
