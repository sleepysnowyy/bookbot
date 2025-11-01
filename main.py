from stats import get_num_words
from stats import get_num_chars
from stats import get_sorted_dict


def get_book_text(filepath: str) -> str:
    filecontents = ""
    with open(filepath) as f:
        filecontents = f.read()
    return filecontents


def main():
    filepath = "books/frankenstein.txt"
    filecontents = get_book_text(filepath)
    sorted_chars = get_sorted_dict(get_num_chars(filecontents))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(filecontents)} total words")
    print("--------- Character Count -------")
    for dict_entry in sorted_chars:
        if dict_entry["char"].isalpha():
            print(f"{dict_entry['char']}: {dict_entry['num']}")


main()
