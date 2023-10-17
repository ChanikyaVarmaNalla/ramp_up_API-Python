def shortest_line_with_words(text, words):
    shortest_line = []
    min_length = float('inf')

    for line in text:
        line_words = line.split()
        line_length = len(line_words)
        if all(word in line_words for word in words):
            if line_length <= min_length:
                min_length = line_length
                shortest_line.append(f"Line {text.index(line) + 1}. {line.strip()}")

    if shortest_line is None:
        return "No line found containing all the words."

    return shortest_line

with open("document1.txt", "r") as rd:
    text_data = rd.readlines()

words_list = ["text", "file", "content"]
result = shortest_line_with_words(text_data, words_list)
print(result)
