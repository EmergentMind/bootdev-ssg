import re

def extract_md_images(md):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", md)
    return matches

def extract_md_links(md):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", md)
    return matches

def extract_stripped_title(md):
    match = re.search(r"^#\s+(.*)", md, re.MULTILINE)
    if match:
      return match.group(1).strip()
    else:
      raise Exception("Provided markdown does not contain a title.")
