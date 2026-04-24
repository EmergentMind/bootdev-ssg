
from classes.textnode import TextType
from classes.htmlnode import LeafNode

def text_node_to_html_node(node):
    match node.text_type:
      case TextType.TEXT:
          return LeafNode(None, node.text)
      case TextType.BOLD:
          return LeafNode("b", node.text)
      case TextType.ITALIC:
          return LeafNode("i", node.text)
      case TextType.CODE:
          return LeafNode("code", node.text)
      case TextType.LINK:
          return LeafNode("a", node.text, {"href": node.url})
      case TextType.IMG:
          return LeafNode("img", "", {"src": node.url, "alt": node.text})
    raise Exception(f"{node.text_type} is not a valid TextType")
