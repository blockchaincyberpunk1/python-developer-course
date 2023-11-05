# Declare variables
name = "John Doe"
age = 25
height = 1.75
lucky_number = 7

# Calculate birth year
current_year = 2023
birth_year = current_year - age

# Calculate age in months and days
age_months = age * 12
age_days = age * 365  # This is a simplified calculation

# Calculate the sum of age and lucky number
age_lucky_sum = age + lucky_number

# Get user input for their favorite color
user_favorite_color = input("Enter your favorite color: ")

# Check if user's favorite color matches mine
my_favorite_color = "Blue"  # You can change this to your actual favorite color
if user_favorite_color.lower() == my_favorite_color.lower():
    color_message = f"We both like {my_favorite_color}!"
else:
    color_message = "Our favorite colors are different."

# Display the results
print("Name:", name)
print("Age:", age)
print("Height:", height, "m")
print("Lucky Number:", lucky_number)
print("Birth Year:", birth_year)
print("Age in Months:", age_months)
print("Age in Days (Approximate):", age_days)
print("Sum of Age and Lucky Number:", age_lucky_sum)
print(color_message)
