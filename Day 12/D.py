from B import B
from C1 import C1

class D(B, C1):
    def __init__(self, name, age, price, qty):
        super().__init__(name, age, price)

        print(self.name)
        print(self.age)
        print(self.price)
        print(self.price * qty)

obj = D("Kunal", 18, 15, 2)