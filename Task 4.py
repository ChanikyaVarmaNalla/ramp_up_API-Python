import re

# Function to extract URLs from a text file
def extract_urls_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            text_data = file.read()
            # Updated regular expression pattern to match URLs
            url_pattern = r'https?://\S+|www\.\S+|\S+\.\S+'
            # Find all matches in the text document
            urls = re.findall(url_pattern, text_data)
            return urls
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []

# Extract URLs from the file
extracted_urls = extract_urls_from_file('urls.txt')

# Print the extracted URLs
for url in extracted_urls:
    print(url)
