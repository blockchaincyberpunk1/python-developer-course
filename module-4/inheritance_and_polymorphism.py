# Step 1: Define the Base Class
# Start by defining a base class (parent class) with attributes and methods.

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        pass  # This method will be overridden in derived classes

# Step 2: Define Derived Classes
# Define one or more derived classes (child classes) that inherit from the base class.

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed

    def speak(self):
        return "Woof!"

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, species="Cat")
        self.color = color

    def speak(self):
        return "Meow!"

# Step 3: Instantiate Objects and Demonstrate Polymorphism
# Create instances (objects) of both the base and derived classes and call methods to demonstrate polymorphism.

# Instantiate objects
animal = Animal("Generic Animal", species="Unknown")
dog = Dog("Buddy", breed="Golden Retriever")
cat = Cat("Whiskers", color="Gray")

# Demonstrate polymorphism by calling the speak method
print(f"{animal.name} says: {animal.speak()}")  # Output: Generic Animal says: No specific sound
print(f"{dog.name} says: {dog.speak()}")          # Output: Buddy says: Woof!
print(f"{cat.name} says: {cat.speak()}")          # Output: Whiskers says: Meow!
