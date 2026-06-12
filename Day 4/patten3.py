for i in range(3):
    for j in range(3):
        if (i+j) % 2 == 0:
            print("X", end=" ")
        else:
            print("O", end=" ")
    print("")
