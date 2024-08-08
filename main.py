def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
    print_report(file_contents)

def count_words(text):
    words = text.split()
    count = 0
    for word in words:
        count += 1
    return count

def count_characters(text):
    result = {}
    for chr in text:
        lower_chr = chr.lower()
        if lower_chr in result:
            result[lower_chr] += 1
        else:
            result[lower_chr] = 1
    return result

def print_report(text):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(text)} words found in the document")
    print("")
    counts = count_characters(text)
    for key in counts:
        if key.isalpha():
            print(f"The '{key}' character was found {counts[key]} times")
    print("--- End report ---")

main()

