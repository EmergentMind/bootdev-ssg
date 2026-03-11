import unittest
from classes.blocktype import BlockType
from block_to_block_type import block_to_block_type

class TestTextNode(unittest.TestCase):
    def test_block_headings(self):
        h1 = "# heading1"
        h2 = "## heading2"
        h3 = "### heading3"
        h4 = "#### heading4"
        h5 = "##### heading5"
        h6 = "###### heading6"
        invalid = "######## not a valid heading"
        result = block_to_block_type(h1)
        self.assertEqual(result, BlockType.HEADING)
        result = block_to_block_type(h2)
        self.assertEqual(result, BlockType.HEADING)
        result = block_to_block_type(h3)
        self.assertEqual(result, BlockType.HEADING)
        result = block_to_block_type(h4)
        self.assertEqual(result, BlockType.HEADING)
        result = block_to_block_type(h5)
        self.assertEqual(result, BlockType.HEADING)
        result = block_to_block_type(h6)
        self.assertEqual(result, BlockType.HEADING)

        result = block_to_block_type(invalid)
        self.assertNotEqual(result, BlockType.HEADING)

    def test_block_code(self):
        code1 = "```\nsome code\n```"
        code2 = "```bash\nsome bash\n```"
        invalid1 = "```invalid block```"
        invalid2 = "`invalid block`"
        result = block_to_block_type(code1)
        self.assertEqual(result, BlockType.CODE)
        result = block_to_block_type(code2)
        self.assertEqual(result, BlockType.CODE)

        result = block_to_block_type(invalid1)
        self.assertNotEqual(result, BlockType.CODE)
        result = block_to_block_type(invalid2)
        self.assertNotEqual(result, BlockType.CODE)

    def test_block_quotes(self):
        quote1 = "> text"
        quote2 = ">text"
        quote3 = "> text\n>text"
        quote4 = ">text\n> text"
        invalid = "# not a quote"
        result = block_to_block_type(quote1)
        self.assertEqual(result, BlockType.QUOTE)
        result = block_to_block_type(quote2)
        self.assertEqual(result, BlockType.QUOTE)
        result = block_to_block_type(quote3)
        self.assertEqual(result, BlockType.QUOTE)
        result = block_to_block_type(quote4)
        self.assertEqual(result, BlockType.QUOTE)

        result = block_to_block_type(invalid)
        self.assertNotEqual(result, BlockType.QUOTE)

    def test_block_ulists(self):
        ulist1 = "- text"
        ulist2 = "- text\n- text"
        invalid1 = "-text"
        invalid2 = "1.text"
        result = block_to_block_type(ulist1)
        self.assertEqual(result, BlockType.UNORDERED_LIST)
        result = block_to_block_type(ulist2)
        self.assertEqual(result, BlockType.UNORDERED_LIST)

        result = block_to_block_type(invalid1)
        self.assertNotEqual(result, BlockType.UNORDERED_LIST)
        result = block_to_block_type(invalid2)
        self.assertNotEqual(result, BlockType.UNORDERED_LIST)

    def test_block_olists(self):
        olist1 = "1. text"
        olist2 = "1. text\n2. text"
        invalid1 = "-text"
        invalid2 = "1.text"
        result = block_to_block_type(olist1)
        self.assertEqual(result, BlockType.ORDERED_LIST)
        result = block_to_block_type(olist2)
        self.assertEqual(result, BlockType.ORDERED_LIST)

        result = block_to_block_type(invalid1)
        self.assertNotEqual(result, BlockType.ORDERED_LIST)
        result = block_to_block_type(invalid2)
        self.assertNotEqual(result, BlockType.ORDERED_LIST)

    def test_block_paragraph(self):
        para1 = "text"
        para2 = "text\ntext"
        invalid1 = "# text"
        invalid2 = "1. text"
        result = block_to_block_type(para1)
        self.assertEqual(result, BlockType.PARAGRAPH)
        result = block_to_block_type(para2)
        self.assertEqual(result, BlockType.PARAGRAPH)

        result = block_to_block_type(invalid1)
        self.assertNotEqual(result, BlockType.PARAGRAPH)
        result = block_to_block_type(invalid2)
        self.assertNotEqual(result, BlockType.PARAGRAPH)
