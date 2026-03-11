import unittest
from classes.textnode import TextNode, TextType
from split_nodes_image import split_nodes_image

class TestTextNode(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMG, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode( "second image", TextType.IMG, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )
    def test_split_images_multinodes(self):
        node1 = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        node2 = TextNode(
            "This is some other text with an ![image](https://foo.bar/baz.png) and some ending text.",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node1, node2])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMG, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode( "second image", TextType.IMG, "https://i.imgur.com/3elNhQu.png"),
                TextNode("This is some other text with an ", TextType.TEXT),
                TextNode("image", TextType.IMG, "https://foo.bar/baz.png"),
                TextNode(" and some ending text.", TextType.TEXT),
            ],
            new_nodes,
        )
    def test_split_no_images(self):
        node = TextNode(
            "This is text with out an image",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with out an image", TextType.TEXT),
            ],
            new_nodes,
        )
    def test_split_non_text_node(self):
        node = TextNode(
            "This is a bold text node",
            TextType.BOLD,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is a bold text node", TextType.BOLD),
            ],
            new_nodes,
        )
