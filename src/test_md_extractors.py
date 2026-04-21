import unittest
from md_extractors import extract_md_images, extract_md_links


class TestTextNode(unittest.TestCase):
    def test_extract_single_md_image(self):
        matches = extract_md_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_multi_md_images(self):
        matches = extract_md_images(
            "This is text with an ![image1](https://foo.png) and another ![image2](https://bar.png)"
        )
        self.assertListEqual([("image1", "https://foo.png"),("image2", "https://bar.png")], matches)


class TestTextNode(unittest.TestCase):

    def test_extract_single_md_link(self):
        matches = extract_md_links(
            "This is text with an [foo](https://foo.bar)"
        )
        self.assertListEqual([("foo", "https://foo.bar")], matches)

    def test_extract_multi_md_links(self):
        matches = extract_md_links(
            "This is text with an [foo](https://foo.bar) and another [baz](https://baz.bar)"
        )
        self.assertListEqual([("foo", "https://foo.bar"),("baz", "https://baz.bar")], matches)


class TestTextNode(unittest.TestCase):

    def test_extract_title(self):
        match = extract_stripped_title(
            """
# This is a title  
## this is a header

followed by a paragraph
```
and a code block
```
"""
        )
        self.assertEqual(match, "This is a title")

    def test_extract_title_with_leading_spaces(self):
        match = extract_stripped_title(
            """
#       This is a title  
## this is a header

followed by a paragraph
```
and a code block
```
"""
        )
        self.assertEqual(match, "This is a title")
