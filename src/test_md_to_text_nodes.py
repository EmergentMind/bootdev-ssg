import unittest
from classes.textnode import TextType
from md_to_text_nodes import md_to_text_nodes

class TestTextNode(unittest.TestCase):
    def test_plain_text(self):
        input_text = "this is some text without nested elements"
        result = md_to_text_nodes(input_text)
        self.assertEqual(result[0].text,"this is some text without nested elements")
        self.assertEqual(result[0].text_type,TextType.TEXT)

    def test_bold_text(self):
        input_text = "this is some text with a nested **bold text** element"
        result = md_to_text_nodes(input_text)
        self.assertEqual(result[0].text, "this is some text with a nested ")
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text, "bold text")
        self.assertEqual(result[1].text_type, TextType.BOLD)
        self.assertEqual(result[2].text, " element")
        self.assertEqual(result[2].text_type, TextType.TEXT)

    def test_bold_italic_text(self):
        input_text = "this is some text with a nested _italic text_ element and some **bold text**."
        result = md_to_text_nodes(input_text)
        self.assertEqual(result[0].text, "this is some text with a nested ")
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text, "italic text")
        self.assertEqual(result[1].text_type, TextType.ITALIC)
        self.assertEqual(result[2].text, " element and some ")
        self.assertEqual(result[2].text_type, TextType.TEXT)
        self.assertEqual(result[3].text, "bold text")
        self.assertEqual(result[3].text_type, TextType.BOLD)
        self.assertEqual(result[4].text, ".")
        self.assertEqual(result[4].text_type, TextType.TEXT)

    def test_code_bold_italic_text(self):
        input_text = "this is some text with a nested _italic text_ element and some **bold text** and some `code text`."
        result = md_to_text_nodes(input_text)
        self.assertEqual(result[0].text, "this is some text with a nested ")
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text, "italic text")
        self.assertEqual(result[1].text_type, TextType.ITALIC)
        self.assertEqual(result[2].text, " element and some ")
        self.assertEqual(result[2].text_type, TextType.TEXT)
        self.assertEqual(result[3].text, "bold text")
        self.assertEqual(result[3].text_type, TextType.BOLD)
        self.assertEqual(result[4].text, " and some ")
        self.assertEqual(result[4].text_type, TextType.TEXT)
        self.assertEqual(result[5].text, "code text")
        self.assertEqual(result[5].text_type, TextType.CODE)
        self.assertEqual(result[6].text, ".")
        self.assertEqual(result[6].text_type, TextType.TEXT)
