from abc import ABC,abstractmethod
class A(ABC):
    def xyz(self):
        print("Hello xyz")
    @abstractmethod
    def show(self):
        pass
class B(A):
    pass
    def show(self):
        print("Show B")
o = B()
o.xyz()
o.show()