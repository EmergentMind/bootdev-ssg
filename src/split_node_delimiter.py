from textnode import TextNode, TextType

def split_node_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.PLAIN:
            new_nodes.append(node)
            continue
        text_parts = node.text.split(delimiter)
        if is_valid_md(text_parts):
            part_nodes = []
            for i in range(0, len(text_parts)):
                part_type = TextType.PLAIN
                if (i+1) % 2 == 0:
                    # every second text_part is of type text_type
                    part_type = text_type
                part_nodes.append(TextNode(text_parts[i], part_type))
            new_nodes.extend(part_nodes)
    return new_nodes

# an even number of node_parts implies the delimiter(s) was not paired
def is_valid_md(list):
    if len(list) % 2 != 0:
        return True
    else:
        raise Exception(
            "Encountered invalid markdown while splitting the node"
        )
