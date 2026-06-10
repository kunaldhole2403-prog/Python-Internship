salary = float(input("Enter monthly salary: "))
cibil = int(input("Enter CIBIL score: "))
existing_loan = float(input("Enter existing loan amount: "))
age = int(input("Enter age: "))

if salary > 25000:
    if cibil > 750:
        if existing_loan < 500000:
            if 21 <= age <= 60:
                print("Loan Eligible")

                if salary > 100000 and cibil > 800:
                    print("Premium Customer Loan Offer")
            else:
                print("Not Eligible: Age Criteria Not Met")
        else:
            print("Not Eligible: Existing Loan Too High")
    else:
        print("Not Eligible: Low CIBIL Score")
else:
    print("Not Eligible: Salary Too Low")
