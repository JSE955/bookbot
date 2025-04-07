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

def sort_on(dict):
    return dict["count"]

def sort_dictionary(dict):
    result = []
    for key in dict:
        item = {}
        item["character"] = key
        item["count"] = dict[key]
        result.append(item)
    result.sort(key=sort_on)
    return result
    