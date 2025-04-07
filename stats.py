def count_words(text):
    return len(text.split())

def char_count(text):
    result = {}
    for char in text:
        char_lower = char.lower()
        if char_lower not in result:
            result[char_lower] = 1
        else:
            result[char_lower] += 1
    return result