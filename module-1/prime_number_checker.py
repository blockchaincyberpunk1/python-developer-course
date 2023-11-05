# Get a positive integer input from the user
try:
    num = int(input("Enter a positive integer: "))
    
    if num <= 0:
        print("Please enter a positive integer.")
    else:
        is_prime = True
        
        # Check if the number is divisible by any integers other than 1 and itself
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        
        # Display whether the number is prime or not
        if num == 1:
            is_prime = False
        if is_prime:
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is not a prime number.")
except ValueError:
    print("Invalid input. Please enter a positive integer.")
