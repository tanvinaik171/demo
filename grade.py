def calculate_grade(marks):
    if marks > 90:
        return "A"
    elif marks > 75
        return "B"
    elif marks > 50:
        return "C"
    else:
        return "Fail"

marks = input("Enter your marks: ")
print("Your grade is: " + calculate_grade(marks))
