import re
from classes.blocktype import BlockType

def get_block_type(md):
    if re.findall(r"(^#{1,6} )", md):
        return BlockType.HEADING
    if re.fullmatch(r"(`{3}.*?\n.*?\n`{3})", md, flags=re.DOTALL):
        return BlockType.CODE
    if re.findall(r"(>{1})", md):
        return BlockType.QUOTE
    if re.findall(r"(-{1} )", md):
        return BlockType.UNORDERED_LIST
    if re.findall(r"(\d\.{1} )", md):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH
