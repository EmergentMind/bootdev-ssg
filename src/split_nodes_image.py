from extract_markdown_images import extract_markdown_images
from classes.textnode import TextNode, TextType

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue
        image_parts = extract_markdown_images(node.text)
        node_parts = []

        cur_str = node.text
        cur_img = 0
        i,j = 0,0
        part = ""
        while i >= 0  and len(cur_str) > 0:
            # find start of next image tag
            i = cur_str.find('!')
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

                # find end of current image tag and caputure remainder of string
                j = cur_str.find(')')
                cur_str = cur_str[j+1:]

        new_nodes.extend(node_parts)
    return new_nodes
