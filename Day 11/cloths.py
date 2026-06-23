from dmart import dmart
class cloths(dmart):
    def __init__(self, category, product_name, qty, price,colour,size):
        super().__init__(category, product_name, qty, price)
        self.colour=colour
        self.size=size

    def display_cloths_details(self):
        print(super().display_store_details())
        print(super().common_features())
        return f" colour{self.colour}\n size{self.size}"
    