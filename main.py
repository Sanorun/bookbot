import sys
from stats import get_num_words
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
   
    sorted_chars = sorted(chars_dict.items(), key=lambda x: x[1], reverse=True)
   
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    
    for char, count in sorted_chars:
        if char.isalpha():
            print(f"{char}: {count}")
    print(f"--- End report of {book_path} ---")

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: {path} not found")
        sys.exit(1)

main()
