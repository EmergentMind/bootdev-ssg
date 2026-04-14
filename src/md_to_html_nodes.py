import re
from classes.blocktype import BlockType
from classes.htmlnode import LeafNode, ParentNode
from classes.textnode import TextType

from md_to_blocks import md_to_blocks
from get_block_type import get_block_type
from md_to_text_nodes import md_to_text_nodes

def md_to_html_nodes(markdown):
  md_block = md_to_blocks(markdown)
  html_blocks = []

  for block in md_block:
    block_type = get_block_type(block)

    match block_type:
      case BlockType.PARAGRAPH:
        html_blocks.append(assemble_html_nodes("p", block))
      case BlockType.HEADING:
        stripped = block.lstrip("#")
        # compare char lengths to determine header level
        level = len(block) - len(stripped)
        # assemble header tag
        tag = "h" + str(level)
        # strip extra spaces too
        html_blocks.append(assemble_html_nodes(tag, stripped.strip()))
      case BlockType.CODE:
        html_blocks.append(md_code_to_html_node(block))
      case BlockType.QUOTE:
        stripped = block.lstrip(">")
        html_blocks.append(assemble_html_nodes("blockquote", stripped))
      case BlockType.UNORDERED_LIST:
        raw_lines = strip_md_list_to_lines(block, block_type)
        wrapped_lines = []
        for line in raw_lines:
          wrapped_lines.append(assemble_html_nodes("li", line))
        wrapped_list = ParentNode("ul", wrapped_lines)
        html_blocks.append(wrapped_list)
      case BlockType.ORDERED_LIST:
        raw_lines = strip_md_list_to_lines(block, block_type)
        wrapped_lines = []
        for line in raw_lines:
          wrapped_lines.append(assemble_html_nodes("li", line))
        wrapped_list = ParentNode("ol", wrapped_lines)
        html_blocks.append(wrapped_list)
  return ParentNode("div", html_blocks)

def assemble_html_nodes(tag, block):
    children = text_to_children(block)
    if children is None:
      return LeafNode(tag, block)
    else:
      return ParentNode(tag, children)

def text_to_children(text):
  # run through splitters
  nodes = md_to_text_nodes(text)

  # length of 1 means there are no children
  if len(nodes) == 1:
    return None
  else:
    children = []
    for node in nodes:
      match node.text_type:
        case TextType.TEXT:
          #replace single newlines with spaces
          flattened = re.sub(r"(?<!\n)\n(?!\n)", " ", node.text)
          children.append(LeafNode(None, flattened))
        case TextType.BOLD:
          children.append(LeafNode("b", node.text))
        case TextType.ITALIC:
          children.append(LeafNode("i", node.text))
        case TextType.CODE:
          children.append(LeafNode("code", node.text))
        case TextType.IMG:
          children.append(LeafNode("img", None, {"src": node.img, "alt": node.text}))
        case TextType.LINK:
          children.append(LeafNode("a", node.text, {"href": node.link}))
    return children

def md_code_to_html_node(block):
  stripped = re.sub(r"(^```\n)|(```$)", "", block)
  #wrap in <code>
  tagged = [LeafNode("code", stripped)]
  #wrap in <pre>
  return ParentNode("pre", tagged)

def strip_md_list_to_lines(block, block_type):
  # split the list items
  lines = block.split("\n")

  list_item_nodes = []
  # convert each list item from md into an html LeafNode
  for line in lines:
    # remove the pre-fixed line item markup
    if block_type == BlockType.ORDERED_LIST:
      stripped = re.sub(r"^\d+[.)]\s+", "", line)
    else:
      stripped = re.sub(r"^\s*[-]\s+", "", line)
    # wrap in <li>
    list_item_nodes.append(stripped)

  return list_item_nodes
