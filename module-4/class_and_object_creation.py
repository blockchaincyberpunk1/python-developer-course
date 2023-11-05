# Step 1: Define Classes
# Start by defining two classes with attributes and methods.

# Example 1: Student class
class Student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Major: {self.major}")

# Example 2: BankAccount class
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance.")

# Step 2: Instantiate Objects
# Create instances (objects) of the defined classes with different attribute values.

# Instantiate Student objects
student1 = Student("Alice", 20, "Computer Science")
student2 = Student("Bob", 22, "Engineering")

# Instantiate BankAccount objects
account1 = BankAccount("123456", 1000)
account2 = BankAccount("789012", 500)

# Step 3: Interact with Objects
# Call methods and modify attributes of the objects.

# Interact with Student objects
student1.display_info()
student2.display_info()

# Interact with BankAccount objects
account1.deposit(500)
account2.withdraw(200)

# Step 4: Display Results
# Use the print() function to display the results of object interactions.

# Display Student information
print("Student 1:")
student1.display_info()
print("\nStudent 2:")
student2.display_info()

# Display BankAccount information
print("\nAccount 1 - Balance:", account1.balance)
print("Account 2 - Balance:", account2.balance)

# Step 5: Run the Program
# Save the Python program to a .py file (e.g., class_and_object_creation.py) and run it to verify the results.

# End of the program
