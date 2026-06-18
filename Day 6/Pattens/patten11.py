n = 5

for i in range(n):
    for j in range(n):
        if i == 0 or i == n//2 or i == n-1:
            print("*", end="")
        elif i < n//2 and j == 0:
            print("*", end="")
        elif i > n//2 and j == n-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()