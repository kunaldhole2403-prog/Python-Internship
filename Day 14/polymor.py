class payment:
    def pay(self):
        pass
    print("payment process started")
class upi(payment):
    def pay(self):
        return "payment done by upi"
    
class gpay(payment):
    def pay(self):
        return "payment done by gpay"
    
u=upi()
g=gpay()
print(u.pay())
print(g.pay())