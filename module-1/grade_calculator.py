# Get input from the user for the scores and weights
homework_score = float(input("Enter homework score (out of 100): "))
homework_weight = float(input("Enter homework weight (as a decimal, e.g., 0.2 for 20%): "))

quizzes_score = float(input("Enter quizzes score (out of 100): "))
quizzes_weight = float(input("Enter quizzes weight (as a decimal, e.g., 0.3 for 30%): "))

exams_score = float(input("Enter exams score (out of 100): "))
exams_weight = float(input("Enter exams weight (as a decimal, e.g., 0.5 for 50%): "))

# Calculate the weighted sum to determine the final grade
final_grade = (homework_score * homework_weight) + (quizzes_score * quizzes_weight) + (exams_score * exams_weight)

# Display the final grade
print("\nFinal Grade:", final_grade)

# Determine the letter grade based on the final grade
if final_grade >= 90:
    letter_grade = "A"
elif final_grade >= 80:
    letter_grade = "B"
elif final_grade >= 70:
    letter_grade = "C"
elif final_grade >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

# Display the corresponding letter grade
print("Letter Grade:", letter_grade)
