class bank:
    def __init__(self,name,ifsc):
        self.name = name
        self.ifsc = ifsc
    def display_bank(self):
        print("Bank Name:",self.name)
        print("IFSC Code:",self.ifsc)

