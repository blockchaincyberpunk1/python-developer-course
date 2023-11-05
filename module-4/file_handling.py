# Step 1: Read Data from an Input File
# Open and read data from an input file (e.g., input.txt).

try:
    with open("input.txt", "r") as file:
        data = file.readlines()
except FileNotFoundError:
    print("Input file not found. Make sure 'input.txt' exists.")
    exit()

# Step 2: Process the Data
# Process the data by calculating the sum of numbers in the file.

try:
    numbers = [int(line.strip()) for line in data]
    total = sum(numbers)
except ValueError:
    print("Error: Input file contains non-integer data.")
    exit()

# Step 3: Write Results to an Output File
# Write the total to an output file (e.g., output.txt).

with open("output.txt", "w") as output_file:
    output_file.write(f"Total: {total}")

# Step 4: Display Results
# Display the results of data processing and file writing.

print(f"Sum of numbers in the input file: {total}")
print("Results have been written to 'output.txt'.")
