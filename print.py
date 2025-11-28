def print_header(book_path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

def print_count(num_words):
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

def print_char_list(char_list):
    print("--------- Character Count -------")
    for char_data in char_list:
        character = char_data["char"]
        if character.isalpha():
            count = char_data["num"]
            print(f"{character}: {count}")


def print_report(book_path, num_words, sorted_characters_list):
    print_header(book_path)
    print_count(num_words)
    print_char_list(sorted_characters_list)