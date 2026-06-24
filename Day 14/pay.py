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
    
class payment_mod:
    def payment_pro(self,obj):
        print(obj.pay())
    print("1.upi\n2.gpay\n3.exit")
ch = int(input("enter choice "))
match ch:
    case 1:
        obj=upi()
    case 2:
        obj=gpay()
    case 3:
        exit()
    case _:
        print("invalid")

p=payment_mod()
p.payment_pro(obj)