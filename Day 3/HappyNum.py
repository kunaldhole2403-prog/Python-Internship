num = int(input("Enter a number: "))

while num != 1 and num != 4:
    sum_sq = 0

    while num > 0:
        digit = num % 10
        sum_sq += digit * digit
        num = num // 10

    num = sum_sq

if num == 1:
    print("Happy Number")
else:
    print("Not a Happy Number")
