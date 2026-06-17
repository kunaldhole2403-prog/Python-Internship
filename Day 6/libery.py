books = [
    [1, "Python"],
    [2, "Java"],
    [3, "C Programming"]
]

book = "Java"

for i in books:
    if i[1] == book:
        print("Book Found:", i)