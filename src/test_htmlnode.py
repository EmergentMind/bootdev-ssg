import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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

    def test_leaf_to_html_link(self):
        node = LeafNode("a", "Link text", {"href": "foo.url"})
        self.assertEqual(node.to_html(), '<a href="foo.url">Link text</a>')

class TestParentNode(unittest.TestCase):
    def test_to_html_with_empty_children(self):
        parent_node = ParentNode("div", [])
        self.assertEqual(parent_node.to_html(), "<div></div>")

    def test_to_html_with_child(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_many_children(self):
        child1_node = LeafNode("b", "Bold text")
        child2_node = LeafNode(None, "Normal text")
        child3_node = LeafNode("i", "italic text")
        child4_node = LeafNode(None, "Normal text")
        parent_node = ParentNode("div", [child1_node,
                                         child2_node,
                                         child3_node,
                                         child4_node],)
        self.assertEqual(
            parent_node.to_html(),
            "<div><b>Bold text</b>Normal text<i>italic text</i>Normal text</div>"
        )

    def test_to_html_with_many_children_and_grandchild(self):
        grandchild_node = LeafNode("i", "grandchild")
        child1_node = LeafNode("b", "Bold text")
        child2_node = LeafNode(None, "Normal text")
        child3_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child1_node,
                                         child2_node,
                                         child3_node
                                        ])
        self.assertEqual(
            parent_node.to_html(),
            "<div><b>Bold text</b>Normal text<span><i>grandchild</i></span></div>"
        )

if __name__ == "__main__":
    unittest.main(props)
