salary = float(input("Enter salary: "))
experience = int(input("Enter years of experience: "))
rating = input("Enter performance rating (A/B): ")

bonus = 0

if experience > 5:
    bonus += salary * 0.20

if rating.upper() == "A":
    bonus += salary * 0.10
elif rating.upper() == "B":
    bonus += salary * 0.05

final_salary = salary + bonus

print("Bonus =", bonus)
print("Final Salary =", final_salary)
