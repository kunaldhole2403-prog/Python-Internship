from dmart import dmart
class grocery(dmart):
    def __init__(self,category, product_name, qty, price,brand_name,mfg,exp):
        super().__init__(category, product_name, qty, price)
        self.brand_name=brand_name
        self.mfg=mfg
        self.exp=exp

    def display_grocery_details(self):
        print(super().display_store_details())
        print(super().common_features())
        return f"brand name{self.brand_name}\n mfg{self.mfg}\n exp{self.exp}\n"
    