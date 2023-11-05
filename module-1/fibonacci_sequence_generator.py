# Function to generate the Fibonacci sequence up to n terms
def generate_fibonacci(n):
    fibonacci_sequence = []
    a, b = 0, 1
    
    for _ in range(n):
        fibonacci_sequence.append(a)
        a, b = b, a + b
    
    return fibonacci_sequence

# Get input from the user
try:
    num_terms = int(input("Enter the number of Fibonacci terms to generate: "))
    
    if num_terms <= 0:
        print("Please enter a positive integer.")
    else:
        fibonacci_result = generate_fibonacci(num_terms)
        print("Fibonacci Sequence:")
        print(fibonacci_result)
except ValueError:
    print("Invalid input. Please enter a positive integer.")
