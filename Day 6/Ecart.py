item = [[]]
id = 0
ch = 0
while ch !=7:
    print("1.View Products\n2.Add Product\n3.Upadate value\n4.Delete\n5.Search\n6.Buy")
    ch = int(input("Enter your choice:"))
    match ch:
        case 1:
            if not any(item):
                print("There are no products")
            else:
                for i in item:
                    print(i)
        case 2:
            nPoducts = int(input("Enter the number of product:"))
            n=1
            while n<=nPoducts:
                id+=1
                product = input("Enter product name:")
                quantity = int(input("Enter quantity of product:"))
                sprice = int(input("Enter single product price :"))
                price = sprice*quantity
                item.append([id,product,quantity,sprice,price])
                n+=1
        case 3:
            id = int(input("Enter product Id:"))
            choice=int(input("Press 1:For Update Product / Press 2:For Update Price / Press 3: For Update Both:"))
            if choice == 1:
                product = input("Enter product name:")
                item[id-1][1] = product
            elif choice == 2:
                price = int(input("Enter product price:"))
                item[id-1][4] = price
            elif choice == 3:
                product = input("Enter product name:")
                item[id - 1][1] = product
                price = int(input("Enter product price:"))
                item[id - 1][4] = price
            else:
                print("Invalid choice")
        case 4:
            isfound = False
            id = int(input("Enter product Id:"))
            for i in range(len(item)):
                if item[i][0] == id:
                    isfound = True
                    break
            if isfound == True:
                item.pop(i)
                print("Product deleted successfully")
            else:
                print("Not found")
        case 5:
            isfound = False
            id = int(input("Enter product Id:"))
            for i in range(len(item)):
                if item[i][0] == id:
                    isfound = True
                    break
            if isfound == True:
                print(f"Product is Found Details:ID:{item[i][0]} Product Name:{item[i][1]} Price:{item[i][4]}")
            else:
                print("Not found")
        case 6:
                print("\t================Ecart================\t")
                quansum = 0
                totalprice = 0
                itemcount = 0
                print("Id\tProduct\tQuantity Singleprice Price")
                for i in range(len(item)):
                    print(f"{item[i][0]}\t{item[i][1]}\t\t{item[i][2]}\t\t {item[i][3]}\t{item[i][4]}")
                    quansum += item[i][2]
                    itemcount +=1
                    totalprice += item[i][4]
                gst = totalprice*0.05
                totalamount = gst+totalprice
                print(f"Items:{itemcount}\tQuantity:{quansum}\tTotal Prise:{totalprice}\tTotalAmount with 5% GST:{totalamount}")
        case 7:
            print("Thank you for using Ecart")
        case _:
            print("Invalid choice")
