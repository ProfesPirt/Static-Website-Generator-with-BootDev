from enum import Enum
from leafnode import LeafNode
class TextType(Enum):
    TEXT = "plaintext"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type, url= None):
        self.text = text
        self.text_type = text_type
        self.url = url
    def __eq__(self, other) -> bool:
        if not self.text == other.text:
            return False
        if not self.text_type == other.text_type:
            return False
        if not self.url == other.url:
            return False
        return True
    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
def text_node_to_html_node(text_node: "TextNode") -> "LeafNode":
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode("img","", {"src": text_node.url, "alt": text_node.text})
    raise Exception("Invalid TextType")
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type is not TextType.TEXT:
            new_nodes.append(old_node)
        string_text = old_node.text.split(delimiter)
        if len(string_text) % 2 == 0:
            raise Exception("Incorrect input missing closing delimiter")
        for i in range(len(string_text)):
            if string_text[i] == "":
                continue
            if i % 2 != 0:
                new_nodes.append(TextNode(string_text[i],text_type))
                continue
            new_nodes.append(TextNode(string_text[i], TextType.TEXT))
    return new_nodes
