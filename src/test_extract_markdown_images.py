import unittest
from extract_markdown_images import extract_markdown_images


class TestTextNode(unittest.TestCase):
    def test_extract_single_markdown_image(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_multi_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image1](https://foo.png) and another ![image2](https://bar.png)"
        )
        self.assertListEqual([("image1", "https://foo.png"),("image2", "https://bar.png")], matches)
