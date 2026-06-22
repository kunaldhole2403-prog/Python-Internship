from p1 import p1
from p2 import p2
class c(p1,p2):
    def pqr(self):
        print("From child")
    def p2_show(self):
        return p2.show(self)
    def __init__(self, name,age):
        p1.__init__(self,name)
        p2.__init__(self,age)

    
obj = c("Kunal",18)
obj.xyz()
obj.pqr()
obj.abc()
obj.p2_show()
