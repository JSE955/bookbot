def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()

    print(count_words(file_contents))
    print(count_characters(file_contents))

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

main()

