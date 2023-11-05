# Step 1: Prompt User for Input
# Prompt the user to enter a number.

try:
    user_input = input("Enter a number: ")
except KeyboardInterrupt:
    print("\nOperation canceled by the user.")
    exit()

# Step 2: Attempt to Perform Operations and Handle Exceptions
# Attempt to convert the user input to an integer and perform a mathematical operation.

try:
    num = int(user_input)
    result = 10 / num
except ValueError:
    print("Invalid input. Please enter a valid integer.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# Step 3: Display Results or Error Messages
# Display the results of the operation or error messages.

if 'result' in locals():
    print(f"Result of the operation: {result}")


""" 
Here's how the program works:

It prompts the user to enter a number. If the user presses Ctrl+C (KeyboardInterrupt), it gracefully handles the interruption.

It attempts to convert the user input to an integer and perform a mathematical operation (division by the entered number). If the user enters invalid input (not an integer) or attempts to divide by zero, it handles the exceptions (ValueError and ZeroDivisionError) with informative error messages.

If the operation is successful (no exceptions are raised), it displays the result. Otherwise, it displays the error messages.

"""
