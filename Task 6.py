
def is_palindrome(input_string):
    def clean_string(s):
        return [i.lower() for i in s if i.isalnum()]

    s2 = clean_string(input_string)

    queue = [j for j in s2]
    stack = [j for j in s2]

    c = 0
    while queue and stack:
        if queue.pop(0) == stack.pop():
            c += 1
        else:
            break
    return c == len(s2)

# Example usage
s1 = "A man, a plan, a canal, Panama"
result = is_palindrome("A man, a plan, a canal, Panama")
if result:
    print(f"The given string '{s1}' is a palindrome")
else:
    print(f"The given string '{s1}' is not a palindrome")
