# Create two lists
numbers = [10, 20, 30, 40, 50]
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Append a new integer value to the numbers list
numbers.append(60)

# Extend the numbers list with another list of integers
numbers.extend([70, 80, 90])

# Slice the numbers list to create a new list with the middle three values
middle_numbers = numbers[1:4]

# Sort the numbers list in ascending order
numbers.sort()

# Append a new fruit name to the fruits list
fruits.append("fig")

# Extend the fruits list with another list of fruit names
fruits.extend(["grape", "honeydew", "kiwi"])

# Slice the fruits list to create a new list with the first three fruit names
first_three_fruits = fruits[:3]

# Sort the fruits list in alphabetical order
fruits.sort()

# Use list comprehensions to filter even numbers from the numbers list
even_numbers = [num for num in numbers if num % 2 == 0]

# Use list comprehensions to convert fruit names to uppercase in the fruits list
uppercase_fruits = [fruit.upper() for fruit in fruits]

# Display the results
print("Updated Numbers List:", numbers)
print("Middle Numbers List:", middle_numbers)
print("Even Numbers List:", even_numbers)
print("Updated Fruits List:", fruits)
print("First Three Fruits List:", first_three_fruits)
print("Uppercase Fruits List:", uppercase_fruits)
