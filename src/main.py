import sys

from static_to_public import file_copier
from generate_page import generate_pages_recursive

def main():
  # use cli args to get basepath
  if len(sys.argv) > 1:
    basepath = sys.argv[1]
  else:
    basepath = "/"

  file_copier("static", "docs")
  generate_pages_recursive("content", "template.html", "docs", basepath)

if __name__ == "__main__":
    main()
