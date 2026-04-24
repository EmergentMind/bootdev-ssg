from md_extractors import extract_md_images, extract_md_links
from classes.textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue
        text_parts = node.text.split(delimiter)
        if is_valid_md(text_parts):
            part_nodes = []
            for i in range(0, len(text_parts)):
                part_type = TextType.TEXT
                if (i+1) % 2 == 0:
                    # every second text_part is of type text_type
                    part_type = text_type
                if text_parts[i] =="":
                    continue
                else:
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

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue
        image_parts = extract_md_images(node.text)
        node_parts = []

        cur_str = node.text
        cur_img = 0
        i,j = 0,0
        part = ""
        while i >= 0  and len(cur_str) > 0:
            # find start of next image tag
            i = cur_str.find('![')
            if i == -1:
                # no image tag found
                part = TextNode(cur_str, TextType.TEXT)
                node_parts.append(part)
            else:
                # add text data as a part
                part = TextNode(cur_str[0:i], TextType.TEXT)
                node_parts.append(part)
                # add extracted image as a part
                part = TextNode(image_parts[cur_img][0],
                                TextType.IMG,
                                image_parts[cur_img][1])
                node_parts.append(part)
                cur_img += 1

                # find end of current image tag and capture remainder of string
                j = cur_str.find(')')
                cur_str = cur_str[j+1:]

        new_nodes.extend(node_parts)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue
        link_parts = extract_md_links(node.text)
        node_parts = []

        cur_str = node.text
        cur_link = 0
        i,j = 0,0
        part = ""
        while i >= 0  and len(cur_str) > 0:
            # find start of next link tag
            i = cur_str.find('[')
            if i == -1:
                # no link tag found
                part = TextNode(cur_str, TextType.TEXT)
                node_parts.append(part)
            else:
                # add text data as a part
                part = TextNode(cur_str[0:i], TextType.TEXT)
                node_parts.append(part)
                # add extracted link as a part
                part = TextNode(link_parts[cur_link][0],
                                TextType.LINK,
                                link_parts[cur_link][1])
                node_parts.append(part)
                cur_link += 1

                # find end of current link tag and capture remainder of string
                j = cur_str.find(')')
                cur_str = cur_str[j+1:]

        new_nodes.extend(node_parts)
    return new_nodes
