import sys

from stats import character_counts, count_words, sort_character_map
from print import print_report

def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
        return file_contents

def main(book_path):
    text = get_book_text(book_path)
    num_words = count_words(text)
    character_map = character_counts(text)
    sorted_characters_list = sort_character_map(character_map)

    print_report(book_path, num_words, sorted_characters_list)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    main(book_path)