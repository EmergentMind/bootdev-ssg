import os
from md_to_html_node import md_to_html_node
from md_extractors import extract_stripped_title

def generate_page(from_path, template_path, dest_path):
  print(f"Generating page from {from_path} to {dest_path} using {template_path}.")
  md = read_file(from_path)
  page = read_file(template_path)

  title = extract_stripped_title(md)
  content = md_to_html_node(md).to_html()

  page = page.replace("{{ Title }}", title).replace("{{ Content }}", content)

  write_file(dest_path, page)

def read_file(path):
  with open(path) as f:
    return f.read()

def write_file(path, content):
  dest_dirs = os.path.dirname(path)
  os.makedirs(dest_dirs, exist_ok=True)
  with open(path, 'w') as f:
    f.write(content)

def generate_pages_recursive(dir_path, template_path, dest_dir_path):
  src_contents = os.listdir(dir_path)
  for item in src_contents:
    cur_path = os.path.join(dir_path, item)
    if os.path.isfile(cur_path):
      if item.endswith('.md'):
        item_name_as_html = item.rstrip('.md') + ".html"
        dest_path = os.path.join(dest_dir_path, item_name_as_html)
        from_path = os.path.join(dir_path, item)
        generate_page(from_path, template_path, dest_path)
    else:
      nest_src_path = os.path.join(dir_path, item)
      nested_dest_path = dest_dir_path + '/' + item
      generate_pages_recursive(nest_src_path, template_path, nested_dest_path)

