class account:
    def __init__(self,bal):
        self.__bal=bal

    def get_bal(self):
        return self.__bal
    
    def set_bal(self,amt):
        self.__bal=amt
        print("bal updated")

    def __private_method(self):
        print("private method")

    def access_pm(self):
        return self.__private_method()
    
    def __withdraw_amt(self,wamt):
        if self.__bal>wamt:
            self.__bal-=wamt
            print("remaining balance")
            print("withdraw succesful")
        else:
            print("less balance")

    def withdraw(self,amt):
        return self.__withdraw_amt(amt)
    
    def __deposite_amt(self,depo_amt):
        self.__bal+=depo_amt
        print("new balanace")

    def depo(self,amt):
        return self.__deposite_amt(amt)

obj = account(1000)
print(obj.get_bal())
obj.set_bal(500)
print(obj.get_bal())
print(obj.access_pm())
print(obj.withdraw(18))
print(obj.get_bal())
print(obj.depo(18))
print(obj.get_bal())