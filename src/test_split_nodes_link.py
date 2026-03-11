import unittest
from classes.textnode import TextNode, TextType
from split_nodes_link import split_nodes_link

class TestTextNode(unittest.TestCase):
    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://foo.bar) and another [second link](https://baz.bar)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://foo.bar"),
                TextNode(" and another ", TextType.TEXT),
                TextNode( "second link", TextType.LINK, "https://baz.bar"),
            ],
            new_nodes,
        )
    def test_split_links_multinodes(self):
        node1 = TextNode(
            "This is text with a [link](https://foo.bar) and another [second link](https://baz.bar)",
            TextType.TEXT,
        )
        node2 = TextNode(
            "This is some other text with a [link](https://foo.bar) and some ending text.",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node1, node2])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://foo.bar"),
                TextNode(" and another ", TextType.TEXT),
                TextNode( "second link", TextType.LINK, "https://baz.bar"),
                TextNode("This is some other text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://foo.bar"),
                TextNode(" and some ending text.", TextType.TEXT),

            ],
            new_nodes,
        )
    def test_split_no_links(self):
        node = TextNode(
            "This is text with out a link",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with out a link", TextType.TEXT),
            ],
            new_nodes,
        )
    def test_split_non_text_node(self):
        node = TextNode(
            "This is a bold text node",
            TextType.BOLD,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is a bold text node", TextType.BOLD),
            ],
            new_nodes,
        )
