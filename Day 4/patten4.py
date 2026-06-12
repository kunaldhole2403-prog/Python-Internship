k = 1
for i in range(1,4):
    print(" " * (3-i),end="")
    for j in range(1,i*2):
        print(k,end=" ")
    print("")
    k+=2
k=3
for a in range(1,3):
    print(" " * (a),end="")
    for b in range(1,6-(2*a)):
        print(k,end=" ")
    print("")
    k-=2
