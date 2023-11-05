import random

def guess_the_number():
    # Generate a random number between 1 and 100
    target_number = random.randint(1, 100)
    
    attempts = 0

    while True:
        user_guess = input("Guess the number between 1 and 100: ")
        attempts += 1

        try:
            user_guess = int(user_guess)
            
            if user_guess == target_number:
                print(f"Congratulations! You guessed the number {target_number} in {attempts} attempts.")
                break
            elif user_guess < target_number:
                print("Try a higher number.")
            else:
                print("Try a lower number.")
        except ValueError:
            print("Invalid input. Please enter a valid number between 1 and 100.")

    play_again = input("Do you want to play again? (yes/no): ")
    
    return play_again.lower() == "yes"

while guess_the_number():
    pass
