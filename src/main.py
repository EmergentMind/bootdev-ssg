from static_to_public import file_copier
from generate_page import generate_pages_recursive

def main():
  file_copier("static", "public")
  generate_pages_recursive("content", "template.html", "public")

if __name__ == "__main__":
    main()
