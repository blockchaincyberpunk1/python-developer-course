# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Division by zero is not allowed"
    else:
        return x / y

# Main program
while True:
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'exit' to end the program")

    user_input = input(": ")

    if user_input == "exit":
        print("Exiting the program.")
        break
    elif user_input in ["add", "subtract", "multiply", "divide"]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if user_input == "add":
            result = add(num1, num2)
            print("Result:", result)
        elif user_input == "subtract":
            result = subtract(num1, num2)
            print("Result:", result)
        elif user_input == "multiply":
            result = multiply(num1, num2)
            print("Result:", result)
        elif user_input == "divide":
            result = divide(num1, num2)
            print("Result:", result)
    else:
        print("Invalid input. Please enter a valid option.")
