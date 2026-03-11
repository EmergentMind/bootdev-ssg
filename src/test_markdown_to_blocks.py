import unittest
from markdown_to_blocks import markdown_to_blocks

class TestTextNode(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    def test_markdown_to_blocks_empty_blocks(self):
        md = """
This is a paragraph





This is another paragraph after some excessive new lines
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is a paragraph",
                "This is another paragraph after some excessive new lines",
            ],
        )
    def test_markdown_to_blocks_extra_spaces(self):
        md = """
 This is a paragraph 

 This is another paragraph. Both of them start with spaces before and after. 
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is a paragraph",
                "This is another paragraph. Both of them start with spaces before and after.",
            ],
        )
