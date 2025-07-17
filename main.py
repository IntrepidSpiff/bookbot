import sys
from stats import get_word_count
from stats import get_character_count
from stats import sort_character_count

def get_book_text(fp):
    with open(fp) as fp_open:
        fp_string = fp_open.read()
    return fp_string

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_link = sys.argv[1]
    book_text = get_book_text(book_link)
    book_chars = get_character_count(book_text)
    book_sorted = sort_character_count(book_chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_link}...")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count(book_text)} total words")
    print("--------- Character Count -------")
    for i in book_sorted:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")

main()