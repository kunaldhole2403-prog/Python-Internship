num = int(input("Enter a number: "))

original = num
sum_fact = 0

while num > 0:
    digit = num % 10

    fact = 1
    for i in range(1, digit + 1):
        fact *= i

    sum_fact += fact
    num = num // 10

if sum_fact == original:
    print("Strong Number")
else:
    print("Not a Strong Number")
