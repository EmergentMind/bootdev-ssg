def md_to_blocks(markdown):
    return remove_empties( list(map(stripper, markdown.split("\n\n") ) ) )

def stripper(str):
    return str.strip()

def remove_empties(blocks):
    return list(filter(lambda b: len(b) > 0, blocks))
