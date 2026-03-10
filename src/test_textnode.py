import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq_partial_args(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_all_args(self):
        node = TextNode("This is a text node", TextType.BOLD, "foo.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "foo.com")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, "foo.com")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_different_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is another text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_different_types(self):
        node = TextNode("This is a text node", TextType.LINK, "foo.com")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
