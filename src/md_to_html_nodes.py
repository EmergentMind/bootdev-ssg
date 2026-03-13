from md_to_blocks import md_to_blocks

def markdown_to_html_node(markdown):
  #split markdown to blocks with existing functison
  md_blocks = md_to_blocks(markdown)

  #loop over each block:
    # 1. determine type of block with existing
    # 2. create HTMLNode with proper data
    # 3. assign proper child HTMLNode obj to the block node
    # 4. special case for `code` block

  # Make all block nodes child of a single parent HTML node (div), return it
  # unit tests
