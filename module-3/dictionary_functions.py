# Create two dictionaries
student_info = {"name": "John Doe", "age": 25, "major": "Computer Science"}
employee_info = {"name": "Jane Smith", "employee_id": "EMP12345", "department": "HR"}

# Access and display values associated with specific keys
student_name = student_info["name"]
print("Student Name:", student_name)

# Modify a value
student_info["age"] = 26

# Add a new key-value pair
student_info["gender"] = "Male"

# Delete a key-value pair
del employee_info["employee_id"]

# Iterate through keys and values
print("\nStudent Information:")
for key, value in student_info.items():
    print(f"{key}: {value}")

print("\nEmployee Information:")
for key, value in employee_info.items():
    print(f"{key}: {value}")
