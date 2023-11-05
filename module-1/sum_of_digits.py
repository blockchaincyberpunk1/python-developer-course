# Get input from the user
try:
    num = int(input("Enter a positive integer: "))
    
    if num < 0:
        print("Please enter a positive integer.")
    else:
        # Calculate the sum of digits
        digit_sum = 0
        while num > 0:
            digit_sum += num % 10
            num //= 10
        
        print(f"Sum of digits: {digit_sum}")
except ValueError:
    print("Invalid input. Please enter a positive integer.")
