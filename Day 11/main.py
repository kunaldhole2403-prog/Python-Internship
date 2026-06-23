from cloths import cloths
from grocery import grocery


c=cloths("cloths","shirt",100,799,"black","xl")
obj=grocery("grocery section", "sugar",60,100,"$ugar","2026-06-01","2027-06-01")
lst=[]
while True:
    print("welcome to dmart\n 1.grocery\n 2.cloths\n 3.purchase item\n 4.exit")
    choice=int(input("enter your choice"))
    match choice:
        case 1:
            print(obj.display_grocery_details())
        case 2:
            print(c.display_cloths_details)
        case 3:
            
            print("1.cloths\n 2.grocery\n 3.generate bill\n 4.exit")
            ch=int(input("enter your choice"))
            

            match ch:
                case 1:
                    qt=int(input("enter quantity"))
                    totalprice=qt*c.price
                    lst.append([c.product_name,qt,c.price,totalprice])
                    print(lst)
                case 2:
                    qt=int(input("enter quantity"))
                    totalprice=qt*obj.price
                    lst.append([obj.brand_name,qt,obj.price,totalprice])
                    print(lst)
                case 3:
                    if not lst:
                        print("cart empty!")
                    else:
                        print("Produt name\tquantity\tOriginal price\ttotal price")
                        print("---------------------------")
                        total=0
                        for item in range (len(lst)):
                            total += lst[item][3]
                            print(f"{lst[item][0]}\t{lst[item][1]}\t{lst[item][2]}\t{lst[item][3]}")
                        print(f"--------total---------{total}")
                         
                case _:
                    print("invalid choice")

        case 4:
            print("thank you for visiting!")
            break
        case _:
            print("invalid choice")