try:
    examination_score = float(input("Enter examination score: "))
    print("Examination Score: ", examination_score)

except ValueError:
    print("Invalid input. Please enter a number.")

if 0 <= examination_score <= 100:
    print("Valid Examination Score")

else:
    print("Invalid input. Please enter a number.")