from account import account

class saving_acc(account):
    def __init__(self, name, IFSC, acc_no, acc_hold, bal,fd):
        super().__init__(name, IFSC, acc_no, acc_hold)
        self.bal=bal
        self.fd=fd

    def display3(self):
        super().display2()
        print("Saving account balance: ",self.bal)
        print("FD balance in Saving account: ",self.fd)
    
    
    def check_balance(self):
        print(f"Current Balance: ₹{self.bal}")

    def deposit(self, amount):
        self.bal += amount
        print(f"₹{amount} deposited successfully.")
        print(f"Current Balance: ₹{self.bal}")

    def withdraw(self, amount):
        if amount > self.bal:
            print("Insufficient Balance!")

        elif self.bal - amount < 2500:
            print("Withdrawal not allowed!")
            print("Minimum balance of Rs.2500 must be maintained.")

        else:
            self.bal -= amount
            print(f"Rs.{amount} withdrawn successfully.")
            print(f"Current Balance: ₹{self.bal}")

    def calculate_fd(self, principal, rate, years):
        maturity_amount = principal * (1 + rate / 100) ** years
        print("\nFD Details")
        print("Principal Amount :", principal)
        print("Interest Rate    :", rate, "%")
        print("Years            :", years)
        print("Maturity Amount  : ₹", round(maturity_amount, 2))


obj=saving_acc("SBI",1234,"ab23g","Atharva",600000,1000000)
ch=0
while ch!=6:
        print("Enter your Choice\n1.See entire bank details\n2.See account balance\n3.Deposit money\n4.Withdraw money\n5.FD Amount after maturity\n6.Exit")
        ch=int(input("Enter your choice:"))
        match ch:
            case 1:
                
                obj.display3()
                
            case 2:
                
                obj.check_balance()
                
            case 3:
                
                amt=int(input("Enter the amount to be Deposited:"))
                obj.deposit(amt)
                
            case 4:
                
                amt=int(input("Enter the amount to be Deposited:"))
                obj.withdraw(amt)
                
            case 5:
                
                principal = float(input("Enter Principal Amount: "))
                rate = float(input("Enter Interest Rate (%): "))
                years = int(input("Enter Number of Years: "))
                obj.calculate_fd(principal, rate, years)
                
            case 6:
                
                print("Exiting..")
                