import unittest
from extract_markdown_links import extract_markdown_links


class TestTextNode(unittest.TestCase):

    def test_extract_single_markdown_link(self):
        matches = extract_markdown_links(
            "This is text with an [foo](https://foo.bar)"
        )
        self.assertListEqual([("foo", "https://foo.bar")], matches)

    def test_extract_multi_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with an [foo](https://foo.bar) and another [baz](https://baz.bar)"
        )
        self.assertListEqual([("foo", "https://foo.bar"),("baz", "https://baz.bar")], matches)
