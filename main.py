from stats import count_words, char_count

def get_book_text(filepath):
    with open(filepath) as book:
        return book.read()
    
def main():
    book_text = get_book_text("./books/frankenstein.txt")
    count = char_count(book_text)
    print(f"{count_words(book_text)} words found in the document")
    print(count)

main()