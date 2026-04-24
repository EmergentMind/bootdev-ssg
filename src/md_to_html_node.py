from classes.blocktype import BlockType
from classes.htmlnode import LeafNode, ParentNode
from classes.textnode import TextType, TextNode

from text_node_to_html_node import text_node_to_html_node
from md_to_blocks import md_to_blocks
from get_block_type import get_block_type
from md_to_text_nodes import md_to_text_nodes

def md_to_html_node(markdown):
  blocks = md_to_blocks(markdown)
  children = []
  for block in blocks:
    html_node = block_to_html_node(block)
    children.append(html_node)
  return ParentNode("div", children, None)

def block_to_html_node(block):
    block_type = get_block_type(block)
    match block_type:
      case BlockType.PARAGRAPH:
        return paragraph_to_html_node(block)
      case BlockType.HEADING:
        return heading_to_html_node(block)
      case BlockType.CODE:
        return code_to_html_node(block)
      case BlockType.QUOTE:
        return quote_to_html_node(block)
      case BlockType.UNORDERED_LIST:
        return ulist_to_html_node(block)
      case BlockType.ORDERED_LIST:
        return olist_to_html_node(block)
    raise ValueError("invalid block type")

def assemble_html_node(tag, block):
  # run through splitters
  text = md_to_text_nodes(block)

  # length of 1 means there are no children
  if len(text) == 1:
    if tag != "p":
      value = text_node_to_html_node(text[0])
    return LeafNode(tag, value)
  else:
    children = text_to_children(text)
    return ParentNode(tag, children)

def text_to_children(text):
  text_nodes = md_to_text_nodes(text)
  children = []
  for text_node in text_nodes:
    html_node = text_node_to_html_node(text_node)
    children.append(html_node)
  return children

def paragraph_to_html_node(block):
  lines = block.split("\n")
  paragraph = " ".join(lines)
  children = text_to_children(paragraph)
  return ParentNode("p", children)

def heading_to_html_node(block):
  stripped = block.lstrip("#")
  # compare char lengths to determine header level
  level = len(block) - len(stripped)
  # assemble header tag
  tag = "h" + str(level)
  children = text_to_children(stripped.strip())
  return ParentNode(tag, children)

def quote_to_html_node(block):
  lines = block.split("\n")
  new_lines = []
  for line in lines:
    if not line.startswith(">"):
      raise ValueError("Invalid quote block")
    new_lines.append(line.lstrip(">").strip())
  content = " ".join(new_lines)
  children = text_to_children(content)
  return ParentNode("blockquote", children)

def ulist_to_html_node(block):
  lines = block.split("\n")
  html_lines = []
  for line in lines:
    text = line[2:]
    children = text_to_children(text)
    html_lines.append(ParentNode("li", children))
  return ParentNode("ul", html_lines)

def olist_to_html_node(block):
  lines = block.split("\n")
  html_lines = []
  for line in lines:
    line_parts = line.split(". ", 1)
    text = line_parts[1]
    children = text_to_children(text)
    html_lines.append(ParentNode("li", children))
  return ParentNode("ol", html_lines)

def code_to_html_node(block):
  if not block.startswith("```") or not block.endswith("```"):
      raise ValueError("invalid code block")
  stripped = block[4:-3]
  raw_text_node = TextNode(stripped, TextType.TEXT)
  leaf = text_node_to_html_node(raw_text_node)
  tagged = ParentNode("code", [leaf])
  return ParentNode("pre", [tagged])

