# Function to calculate factorial using recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Get input from the user
try:
    num = int(input("Enter a positive integer: "))
    
    if num < 0:
        print("Please enter a positive integer.")
    else:
        result = factorial(num)
        print(f"{num}! = {result}")
except ValueError:
    print("Invalid input. Please enter a positive integer.")
