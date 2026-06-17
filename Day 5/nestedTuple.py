tup = ([1,2,3], 90,70,[10,20,30])

for i in tup:
    if type(i) == tuple: 
        for item in i:
            print(item)
    elif type(i) == list: 
        for item in i:
            print(item)
    else:
        print(i)