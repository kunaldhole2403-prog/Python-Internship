class Engine:
    def __init__(self, chessno,horsepower):
        self.chessno = chessno
        self.horsepower = horsepower
    def display_engine(self):
        return f"{self.chessno},{self.horsepower}"
class Car:
    def __init__(self,name,price):
           self.name = name
           self.price = price
           self.engine = Engine(355,500)
    def display_car(self):
         return f"{self.name},{self.price}"
    
    def display_all_details(self):
         print(self.display_car())
         print(self.engine.display_engine())
car_obj = Car("BMW","1cr")
car_obj.display_all_details()