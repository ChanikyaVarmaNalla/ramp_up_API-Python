import re

def read_document(file_path):
    try:
        with open(file_path, "r") as file:
            read_data = file.read()
        return read_data
    except FileNotFoundError:
        print(f"File not found: {file_path}\n")

def extract_sequences(document):
    # Define a regular expression pattern to match the desired sequences
    pattern = r"Start(\n.*?)End"

    # Use re.findall to find all matching sequences in the document
    matches = re.findall(pattern, document, re.DOTALL)

    return matches

if __name__ == "__main__":
    data = read_document("document.txt")

    if data:
        sequences = extract_sequences(data)

        # Print the extracted sequences
        for i, sequence in enumerate(sequences, start=1):
            print(f"Sequence {i}:\n{sequence.strip()}\n")
