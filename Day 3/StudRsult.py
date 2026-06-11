
for i in range(1, 6):
    print("\nStudent", i)

    total = 0

    for j in range(1, 6):
        marks = float(input(f"Enter marks of Subject {j}: "))
        total += marks

    percentage = total / 5

    if percentage >= 90:
        grade = "A"
    elif percentage >= 75:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    else:
        grade = "Fail"

    print("Total Marks =", total)
    print("Percentage =", percentage)
    print("Grade =", grade)
