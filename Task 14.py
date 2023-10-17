def can_split_string(string, valid_words):
    if not string:
        return True

    for word in valid_words:
        if string.startswith(word):
            new_string = string[len(word):]
            new_valid_words = [w for w in valid_words if w != word]
            if can_split_string(new_string, new_valid_words):
                return True
    return False

# Example usage:
string = "applepie"
valid_words = ["apple", "pie", "app", "le", "p"]
print(can_split_string(string, valid_words))
