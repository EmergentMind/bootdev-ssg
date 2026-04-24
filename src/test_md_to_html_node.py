import unittest
from md_to_html_node import md_to_html_node

class TestTextNode(unittest.TestCase):
  def test_paragraphs(self):
    md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

    node = md_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
    )

  def test_codeblock(self):
    md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

    node = md_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
    )

  def test_quoteblock(self):
    md = """
>This is some quoted text that _should_ have inline **formatting**
"""

    node = md_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><blockquote>This is some quoted text that <i>should</i> have inline <b>formatting</b></blockquote></div>",
    )

  def test_ulist(self):
    md = """
- This is an
- unordered list
"""

    node = md_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><ul><li>This is an</li><li>unordered list</li></ul></div>",
    )

  def test_olist(self):
    md = """
1. This is an
2. ordered list
"""

    node = md_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><ol><li>This is an</li><li>ordered list</li></ol></div>",
  )

  def test_h1(self):
    md = """
# h1
"""

    node = md_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><h1>h1</h1></div>",
    )
  def test_h2(self):
    md = """
## h2
"""

    node = md_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><h2>h2</h2></div>",
    )
  def test_h5(self):
    md = """
##### h5
"""

    node = md_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><h5>h5</h5></div>",
    )
  def test_not_a_header(self):
    md = """
####### not a header
"""

    node = md_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><p>####### not a header</p></div>",
    )
