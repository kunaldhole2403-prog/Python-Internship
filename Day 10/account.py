from bank import bank
class account(bank):
    def __init__(self, name, ifsc,acc_no,acc_hold):
        super().__init__(name, ifsc)
        self.acc_no = acc_no
        self.acc_hold = acc_hold
    def diaplay_account(self):
        super().display_bank()
        print("Account Holder Name:",self.AHname)
        print("Account No:",self.Ano)
