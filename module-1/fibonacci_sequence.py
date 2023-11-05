# Get the number of terms for the Fibonacci sequence from the user
num_terms = int(input("Enter the number of terms for the Fibonacci sequence: "))

# Initialize the first two terms of the sequence
a, b = 0, 1

# Initialize a list to store the Fibonacci sequence
fib_sequence = []

# Generate and display the Fibonacci sequence
for _ in range(num_terms):
    fib_sequence.append(a)  # Add the current term to the sequence
    a, b = b, a + b  # Calculate the next term

# Display the generated Fibonacci sequence
print("Fibonacci Sequence:")
for term in fib_sequence:
    print(term, end=" ")
