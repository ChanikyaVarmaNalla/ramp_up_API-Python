import re

# Read the contents of the "code_blocks.txt" file
with open("code_blocks.txt", "r") as file:
    code_blocks = file.read()

# Regular expression pattern to match function definitions in Python
python_function_pattern = r"def\s+([a-zA-Z_]\w*)\s*\(([^)]*)\)"

# Regular expression pattern to match function definitions in Java
java_function_pattern = r"public\s+int\s+([a-zA-Z_]\w*)\s*\(([^)]*)\)"

# Regular expression pattern to match function definitions in C++
cpp_function_pattern = r"(\w+)\s+([a-zA-Z_]\w*)\s*\(([^)]*)\)"

# Split the code blocks by language
code_blocks = code_blocks.strip().split("\n\n")

# Process each code block and print function names and parameters
for code_block in code_blocks:
    if "def" in code_block:
        matches = re.finditer(python_function_pattern, code_block)
        language = "Python"
    elif "public" in code_block:
        matches = re.finditer(java_function_pattern, code_block)
        language = "Java"
    else:
        matches = re.finditer(cpp_function_pattern, code_block)
        language = "C++"

    for match in matches:
        if match.group(1) == "int":
            function_name = match.group(2)
            parameters = match.group(3)
            print(f"Language: {language}, Function: {function_name}, Parameters: {parameters}")
        else:
            function_name = match.group(1)
            parameters = match.group(2)
            print(f"Language: {language}, Function: {function_name}, Parameters: {parameters}")
