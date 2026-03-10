import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_eq_no_args(self):
        node = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node.tag, node2.tag)
        self.assertEqual(node.value, node2.value)
        self.assertEqual(node.children, node2.children)
        self.assertEqual(node.props, node2.props)

    def test_eq_single_args(self):
        node = HTMLNode("h1")
        node2 = HTMLNode("h1")
        self.assertEqual(node.tag, node2.tag)

    def test_eq_double_args(self):
        node = HTMLNode("h1", "this is a heading")
        node2 = HTMLNode("h1", "this is a heading")
        self.assertEqual(node.value, node2.value)

    def test_eq_triple_args(self):
        child_node = HTMLNode("a", "this is a childe node")
        node = HTMLNode(
                "h1",
                "this is heading",
                [child_node],
                )
        node2 = HTMLNode(
                "h1",
                "this is heading",
                [child_node],
                )
        self.assertEqual(node.children, node2.children)

    def test_eq_full_args(self):
        node = HTMLNode(
                "h1",
                "this is heading",
                [HTMLNode("a", "this is a child node")],
                {"foo": "bar"}
                )
        node2 = HTMLNode(
                "h1",
                "this is heading",
                [HTMLNode("a", "this is a child node")],
                {"foo": "bar"}
                )
        self.assertEqual(node.props_to_html(), node2.props_to_html())

    def test_not_eq_no_args(self):
        node = HTMLNode()
        node2 = HTMLNode("foo")
        self.assertNotEqual(node.tag, node2.tag)

    def test_not_eq_single_args(self):
        node = HTMLNode("h1")
        node2 = HTMLNode("h2")
        self.assertNotEqual(node.tag, node2.tag)

    def test_not_eq_double_args(self):
        node = HTMLNode("h1", "this is a heading")
        node2 = HTMLNode("h1", "this is another heading")
        self.assertNotEqual(node.value, node2.value)

    def test_not_eq_triple_args(self):
        node = HTMLNode(
                "h1",
                "this is heading",
                [HTMLNode("a", "this is a child node")],
                )
        node2 = HTMLNode(
                "h1",
                "this is heading",
                [HTMLNode("img", "this is another child node")],
                )
        self.assertNotEqual(node.children, node2.children)

    def test_not_eq_full_args(self):
        node = HTMLNode(
                "h1",
                "this is heading",
                [HTMLNode("a", "this is a child node")],
                {"foo": "bar"}
                )
        node2 = HTMLNode(
                "h1",
                "this is heading",
                [HTMLNode("a", "this is a child node")],
                {"foo": "bar baz"}
                )
        self.assertNotEqual(node.props_to_html(), node2.props_to_html())

class TestHTMLNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_img(self):
        node = LeafNode("a", "Link text", {"href": "foo.url"})
        self.assertEqual(node.to_html(), '<a href="foo.url">Link text</a>')

if __name__ == "__main__":
    unittest.main()
