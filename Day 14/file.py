try:
    file = open("myfile.txt","x")
    print(file)
except Exception as e:
    print(e)

#write
with open("myfile.txt","w") as f:
    f.write("hello i am writing something")
    print("Data Added")

#read
with open("myfile.txt","r") as f:
    data = f.read()
    print(data)