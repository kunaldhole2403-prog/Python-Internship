k = 96
for i in range(3,0,-1):
    k+=1
    for s in range(3-i):
        print(" ",end=" ")
    for j in range(i):
        print(chr(k), end=" ")
    print(" ")
