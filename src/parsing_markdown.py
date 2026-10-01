import re
import textnode
def extract_markdown_images(text):
    return re.findall(r"\!\[(.*?)\]\((.*?)\)", text)
def extract_markdown_link(text):
    return re.findall(r"(?<!\!)\[(.*?)\]\((.*?)\)", text)
def text_to_textnodes(text):
    nodes = [textnode.TextNode(text,textnode.TextType.TEXT)]
    if "**" in text:
        nodes = textnode.split_nodes_delimiter(nodes, "**", textnode.TextType.BOLD)
    if "_" in text:
        nodes = textnode.split_nodes_delimiter(nodes, "_", textnode.TextType.ITALIC)
    if "`" in text:
        nodes = textnode.split_nodes_delimiter(nodes, "`", textnode.TextType.CODE)
    return textnode.split_nodes_link(textnode.split_nodes_image(nodes))