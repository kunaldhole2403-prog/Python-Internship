class Student:
    college = "PCP Pune"    # Class Variable

    def __init__(self, name, age):
        self.name = name    # Instance Variable
        self.age = age      # Instance Variable

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("College:", Student.college)
        print()

# Creating Objects
s1 = Student("Kunal", 18)
s2 = Student("Rahul", 19)

# Displaying Data
s1.display()
s2.display()