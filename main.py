from stats import word_counter, character_count, chars_dict_to_sorted_list
import sys

def main():
    #book_path = "books/frankenstein.txt"

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]

    text = get_book_text(book_path)
    num_words = word_counter(text)
    num_characters = character_count(text)
    chars_list = chars_dict_to_sorted_list(num_characters)
    print(f"{num_words} words found in the document")
    sorted_chars = chars_dict_to_sorted_list(num_characters)
    print_report(book_path, num_words, chars_list)


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents



def print_report(book_path, num_words, chars_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['count']}")

    print("============= END ===============")


main()



