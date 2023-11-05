# Define a list of numbers
numbers = [5, 12, 8, 17, 3, 21]

# Calculate the sum of numbers using a loop
total = 0
for number in numbers:
    total += number

# Calculate the average (mean) of numbers
average = total / len(numbers)

# Find the maximum and minimum values using loops
maximum = numbers[0]
minimum = numbers[0]
for number in numbers:
    if number > maximum:
        maximum = number
    if number < minimum:
        minimum = number

# Display the results
print("List of Numbers:", numbers)
print("Sum of Numbers:", total)
print("Average of Numbers:", average)
print("Maximum Value:", maximum)
print("Minimum Value:", minimum)
