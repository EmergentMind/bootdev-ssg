import unittest
from classes.textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter

class TestTextNode(unittest.TestCase):
    def test_plain_text(self):
        node = TextNode("this is some text without nested elements",
                        TextType.TEXT)
        node2 = TextNode("this is some other text without nested elements",
                        TextType.TEXT)
        new_nodes = split_nodes_delimiter([node, node2], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [node, node2])
        self.assertEqual(new_nodes[0].text,"this is some text without nested elements")
        self.assertEqual(new_nodes[1].text,"this is some other text without nested elements")

    def test_non_plain_text(self):
        node = TextNode("_this is some text without nested elements_",
                        TextType.ITALIC)
        node2 = TextNode("_this is some other text without nested elements_",
                        TextType.ITALIC)
        new_nodes = split_nodes_delimiter([node, node2], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [node, node2])
        self.assertEqual(new_nodes[0].text,"_this is some text without nested elements_")
        self.assertEqual(new_nodes[1].text,"_this is some other text without nested elements_")

    def test_bold_text(self):
        node = TextNode("this is some text with a nested **bold text** element",
                        TextType.TEXT)
        node2 = TextNode("this is some other text without nested elements",
                        TextType.TEXT)
        new_nodes = split_nodes_delimiter([node, node2], "**", TextType.BOLD)
        self.assertNotEqual(new_nodes, [node, node2])
        self.assertEqual(new_nodes[0].text, "this is some text with a nested ")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[1].text, "bold text")
        self.assertEqual(new_nodes[1].text_type, TextType.BOLD)
        self.assertEqual(new_nodes[2].text, " element")
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[3].text, "this is some other text without nested elements")
        self.assertEqual(new_nodes[3].text_type, TextType.TEXT)

    def test_double_bold_text(self):
        node = TextNode("this is some text with **two** nested **bold text** elements",
                        TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertNotEqual(new_nodes, [node])
        self.assertEqual(new_nodes[0].text, "this is some text with ")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[1].text, "two")
        self.assertEqual(new_nodes[1].text_type, TextType.BOLD)
        self.assertEqual(new_nodes[2].text, " nested ")
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[3].text, "bold text")
        self.assertEqual(new_nodes[3].text_type, TextType.BOLD)
        self.assertEqual(new_nodes[4].text, " elements")
        self.assertEqual(new_nodes[4].text_type, TextType.TEXT)

    def test_italic_text(self):
        node = TextNode("this is some text with a nested _italic text_ element",
                        TextType.TEXT)
        node2 = TextNode("this is some other text without nested elements",
                        TextType.TEXT)
        new_nodes = split_nodes_delimiter([node, node2], "_", TextType.ITALIC)
        self.assertNotEqual(new_nodes, [node, node2])
        self.assertEqual(new_nodes[0].text, "this is some text with a nested ")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[1].text, "italic text")
        self.assertEqual(new_nodes[1].text_type, TextType.ITALIC)
        self.assertEqual(new_nodes[2].text, " element")
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[3].text, "this is some other text without nested elements")
        self.assertEqual(new_nodes[3].text_type, TextType.TEXT)

    def test_double_italic_text(self):
        node = TextNode("this is some text with _two_ nested _italic text_ elements",
                        TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertNotEqual(new_nodes, [node])
        self.assertEqual(new_nodes[0].text, "this is some text with ")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[1].text, "two")
        self.assertEqual(new_nodes[1].text_type, TextType.ITALIC)
        self.assertEqual(new_nodes[2].text, " nested ")
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[3].text, "italic text")
        self.assertEqual(new_nodes[3].text_type, TextType.ITALIC)
        self.assertEqual(new_nodes[4].text, " elements")
        self.assertEqual(new_nodes[4].text_type, TextType.TEXT)

    def test_code_text(self):
        node = TextNode("this is some text with a nested `code text` element",
                        TextType.TEXT)
        node2 = TextNode("this is some other text without nested elements",
                        TextType.TEXT)
        new_nodes = split_nodes_delimiter([node, node2], "`", TextType.CODE)
        self.assertNotEqual(new_nodes, [node, node2])
        self.assertEqual(new_nodes[0].text, "this is some text with a nested ")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[1].text, "code text")
        self.assertEqual(new_nodes[1].text_type, TextType.CODE)
        self.assertEqual(new_nodes[2].text, " element")
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[3].text, "this is some other text without nested elements")
        self.assertEqual(new_nodes[3].text_type, TextType.TEXT)

    def test_double_code_text(self):
        node = TextNode("this is some text with `two` nested `code text` elements",
                        TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertNotEqual(new_nodes, [node])
        self.assertEqual(new_nodes[0].text, "this is some text with ")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[1].text, "two")
        self.assertEqual(new_nodes[1].text_type, TextType.CODE)
        self.assertEqual(new_nodes[2].text, " nested ")
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[3].text, "code text")
        self.assertEqual(new_nodes[3].text_type, TextType.CODE)
        self.assertEqual(new_nodes[4].text, " elements")
        self.assertEqual(new_nodes[4].text_type, TextType.TEXT)

