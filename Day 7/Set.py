python={"Ram","Sita","Gita","Rahul"}
mern={"Ram","Ramesh","Gita","Shyam"}

print("Name of all students:",(python | mern))
print("Name of the students who enrolled in both course are:",(python & mern))
print("Name of the students who enrolled only in Python:",(python - mern))
print("Name of the students who enrolled only in MERN:",(mern - python))
print("Name of the students who are not in bot courses",(python ^ mern))