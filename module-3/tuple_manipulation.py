# Define two tuples with different data types
student_info = ("John Doe", 25, "Computer Science")
coordinates = (3.5, 7.2)

# Attempt to modify a tuple (this should result in an error)
try:
    student_info[1] = 26  # This will raise a TypeError
except TypeError as e:
    print(f"Error: {e} (Tuples are immutable)")

# Tuple packing
packed_tuple = 42, "Alice", 3.14

# Tuple unpacking
num, name, pi = packed_tuple

# Display the tuples and results of packing/unpacking
print("Student Info Tuple:", student_info)
print("Coordinates Tuple:", coordinates)
print("Packed Tuple:", packed_tuple)
print("Unpacked Tuple (num, name, pi):", num, name, pi)
