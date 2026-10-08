from enum import Enum
import re
class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

def block_to_block_type(block: str):
    if re.fullmatch(r"#{1,6} [^\n]+", block):
        return BlockType.HEADING
    if re.fullmatch(r"```\n.*```", block, re.DOTALL):
        return BlockType.CODE
    if len(re.findall(r"^> ?.*$", block, re.MULTILINE)) == len(block.split("\n")):
        return BlockType.QUOTE
    if len(re.findall(r"^- .*$", block, re.MULTILINE)) == len(block.split("\n")):
        return BlockType.UNORDERED_LIST
    i = 1
    for line in block.split("\n"):
        if not line.startswith(f"{i}. "):
            return BlockType.PARAGRAPH
        i += 1
    return BlockType.ORDERED_LIST
