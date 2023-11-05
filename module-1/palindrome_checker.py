# Function to check if a string is a palindrome
def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Convert to lowercase and remove spaces
    return s == s[::-1]

# Get input from the user
string_to_check = input("Enter a string: ")

if is_palindrome(string_to_check):
    print(f"'{string_to_check}' is a palindrome.")
else:
    print(f"'{string_to_check}' is not a palindrome.")
