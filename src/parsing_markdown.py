import re
import textnode
import blocks
from leafnode import LeafNode
from parentnode import ParentNode
from htmlnode import HTMLNode

def extract_markdown_images(text):
    return re.findall(r"\!\[(.*?)\]\((.*?)\)", text)
def extract_markdown_link(text):
    return re.findall(r"(?<!\!)\[(.*?)\]\((.*?)\)", text)

def text_to_textnodes(text):
    nodes = [textnode.TextNode(text,textnode.TextType.TEXT)]
    print(nodes)
    if "**" in text:
        nodes = textnode.split_nodes_delimiter(nodes, "**", textnode.TextType.BOLD)
    if "_" in text:
        nodes = textnode.split_nodes_delimiter(nodes, "_", textnode.TextType.ITALIC)
    if "`" in text:
        nodes = textnode.split_nodes_delimiter(nodes, "`", textnode.TextType.CODE)
    return textnode.split_nodes_link(textnode.split_nodes_image(nodes))

def markdown_to_blocks(document):
    return [block.strip() for block in document.split("\n\n") if block != ""]

def text_to_children(text, blocktype):
    children_of_children = [] 
    if blocktype is blocks.BlockType.HEADING:
        for textnodechild in text_to_textnodes(text):
            leafnode = textnode.text_node_to_html_node(textnodechild)
            children_of_children.append(leafnode)
    elif blocktype is blocks.BlockType.PARAGRAPH:
        for textnodechild in text_to_textnodes(text):
            leafnode = textnode.text_node_to_html_node(textnodechild)
            children_of_children.append(leafnode)
    elif blocktype is blocks.BlockType.QUOTE:
        for textnodechild in text_to_textnodes(markdown_to_string(text, blocktype)):
            leafnode = textnode.text_node_to_html_node(textnodechild)
            children_of_children.append(leafnode)
    elif blocktype is blocks.BlockType.UNORDERED_LIST:
        for line in markdown_to_string(text, blocktype).split("\n"):
            textchildren = text_to_textnodes(line)
            children = []
            for text in textchildren:
                children.append(textnode.text_node_to_html_node(text))
            parentnode = ParentNode("li", children)
            children_of_children.append(parentnode)
    else:
        for line in markdown_to_string(text, blocktype).split("\n"):
            textchildren = text_to_textnodes(line)
            children = []
            for text in textchildren:
                children.append(textnode.text_node_to_html_node(text))
                parentnode = ParentNode("li", children)
                children_of_children.append(parentnode)
    return children_of_children
def markdown_to_string(markdown, blocktype):
    new_string = ""
    if blocktype is blocks.BlockType.QUOTE:
        list_of_markdown = markdown.split("\n")
        for line in list_of_markdown:
            if line == list_of_markdown[-1]:
                new_string += line[1:].strip()
                return new_string
            new_string += line[1:].strip() + "\n"
    if blocktype is blocks.BlockType.UNORDERED_LIST:
        list_of_markdown = markdown.split("\n")
        for line in list_of_markdown:
            if line == list_of_markdown[-1]:
                new_string += line[2:] 
                return new_string
            new_string += line[2:] + "\n"
    list_of_markdown = markdown.split("\n")
    for line in list_of_markdown:
        if line == list_of_markdown[-1]:
            new_string += line[3:]
            return new_string
        new_string += line[3:] + "\n"


def markdown_code_to_string(block):
    return [code_string.lstrip() for code_string in block.split("```") if code_string != ""][0]
def markdown_to_html_node(document):
    children: list[HTMLNode] = []
    root_node = ParentNode("div",children)
    for block in markdown_to_blocks(document):
        htmlblock = None
        blocktype = blocks.block_to_block_type(block)
        if blocktype is blocks.BlockType.HEADING:
            htmlblock = ParentNode(f"h{block.count("#",0,6)}", text_to_children(block[block.count("#",0,6)+1:], blocktype))
            children.append(htmlblock)
        elif blocktype is blocks.BlockType.PARAGRAPH:
            print(block)
            htmlblock = ParentNode("p", text_to_children(block.replace("\n"," "), blocktype))
            children.append(htmlblock)
        elif blocktype is blocks.BlockType.QUOTE:
            htmlblock = ParentNode("blockquote",text_to_children(block, blocktype))
            children.append(htmlblock)
        elif blocktype is blocks.BlockType.UNORDERED_LIST:
            htmlblock = ParentNode("ul", text_to_children(block, blocktype))
            children.append(htmlblock)
        elif blocktype is blocks.BlockType.ORDERED_LIST:
            htmlblock = ParentNode("ol", text_to_children(block, blocktype))
            children.append(htmlblock)
        else:
            htmlblock = ParentNode("pre", [textnode.text_node_to_html_node(textnode.TextNode(markdown_code_to_string(block), textnode.TextType.CODE))])
            children.append(htmlblock)
    return root_node
