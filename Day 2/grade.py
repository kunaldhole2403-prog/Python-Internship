total = 0

for i in range(1, 6):
    marks = float(input(f"Enter marks of Subject {i}: "))
    total += marks

percentage = total / 5

print("Percentage =", percentage)

if percentage >= 90:
    print("Grade: A")
    print("Distinction")
elif percentage >= 75:
    print("Grade: B")
    print("Pass")
elif percentage >= 50:
    print("Grade: C")
    print("Pass")
else:
    print("Grade: Fail")
    print("Fail")
