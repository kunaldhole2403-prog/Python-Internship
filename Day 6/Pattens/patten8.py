n = 6


for i in range(n, 0, -1):
    for j in range(n - i):
        print(" ", end="")

    for k in range(1, 2 * i):
        if i == n or i == 1 or k == 1 or k == 2 * i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()


for i in range(2, n + 1):
    for j in range(n - i):
        print(" ", end="")

    for k in range(1, 2 * i):
        if i == n or k == 1 or k == 2 * i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()