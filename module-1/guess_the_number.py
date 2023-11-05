import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Initialize variables
attempts = 0
max_attempts = 10  # You can adjust the number of attempts as desired

print("Welcome to the Guess the Number Game!")
print(f"Guess the number between 1 and 100. You have {max_attempts} attempts.")

while attempts < max_attempts:
    try:
        # Ask the user to guess the number
        guess = int(input("Enter your guess: "))
        
        # Check if the guess is too high or too low
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} correctly in {attempts + 1} attempts.")
            break  # Exit the loop on a correct guess
        
        attempts += 1
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if attempts == max_attempts:
    print(f"Sorry, you've run out of attempts. The secret number was {secret_number}.")
