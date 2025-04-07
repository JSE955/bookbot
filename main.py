from stats import count_words, char_count, sort_dictionary
import sys

def get_book_text(filepath):
    with open(filepath) as book:
        return book.read()
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(sys.argv[1])
    sorted_count = sort_dictionary(char_count(book_text))
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(book_text)} total words")
    print("--------- Character Count -------")
    for item in sorted_count:
        if item["character"].isalpha():
            print(f"{item['character']}: {item['count']}")
    print("============= END ===============")


main()