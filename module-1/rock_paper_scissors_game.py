import random

# List of possible choices
choices = ["rock", "paper", "scissors"]

# Get the user's choice
user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

# Randomly generate the computer's choice
computer_choice = random.choice(choices)

# Display the choices
print(f"\nYour choice: {user_choice}")
print(f"Computer's choice: {computer_choice}\n")

# Determine the winner based on the game's rules
if user_choice == computer_choice:
    result = "It's a tie!"
elif (
    (user_choice == "rock" and computer_choice == "scissors")
    or (user_choice == "scissors" and computer_choice == "paper")
    or (user_choice == "paper" and computer_choice == "rock")
):
    result = "You win!"
else:
    result = "Computer wins!"

# Display the result
print(result)
