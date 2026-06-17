stud = {
    101:{
        "name":"Ram",
        "age":20,
        "sub":("Python","Java","Mern"),
        "Marks":[80,89,87]
    },
    102:{
        "name":"Rohit",
        "age":18,
        "sub":("Python","Java","Mern"),
        "Marks":[90,75,80]   
    },
    103:{
        "name":"Parth",
        "age":19,
        "sub":("Python","Java","Mern"),
        "Marks":[92,85,82]
    },
      104:{
        "name":"Palak",
        "age":18,
        "sub":("Python","Java","Mern"),
        "Marks":[82,85,70]
    }
}

print("\t\t\t===============Students:================")
print("Roll_No\tName\t\tTotal")
for roll, details in stud.items():
    total = sum(details["Marks"])
    print(roll, "\t", details["name"],"\t\t", total)
print("Topper:")
hig_total = 0
for roll,details in stud.items():
    total = sum(details["Marks"])

    if total > hig_total:
        hig_total = total
        stud_topper = details["name"]
print("First rank",stud_topper,"With",hig_total,"Score")
higpy = 0
print("Higest marks in Python:")
for roll,details in stud.items():
    py = details["Marks"][0]
    if py > higpy:
        higpy = py
        higpystud = details["name"]
print(f"{higpystud} has highest marks in python with score:{higpy}")

for roll,details in stud.items():
    age = details["age"]
    if age > 19:
        print(f"Roll no:{roll} Age:{age}")

print("Students Thouse have marks between 70 to 90 in Mern" )
print("Name\tMarks")
for roll,details in stud.items():
    marks = details["Marks"][2]
    if 90>marks>70:
        sname = details["name"]
        print(sname,"\t",marks)