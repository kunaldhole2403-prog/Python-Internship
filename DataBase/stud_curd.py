import sqlite3
conn = sqlite3.connect("student.db")
cursor = conn.cursor()

cursor.execute("""
            create table if not exists stud(
               sid integer primary key,
               name text not null,
               age integer null)
""")

print("Created!")
# sid = int(input("Enter yr Id"))
# sname = input("Enter yr Name")
# age = int(input("Enter yr age"))
# cursor.execute("insert into stud (sid,name,age) values(?,?,?)",(sid,sname,age))
# conn.commit()
# print(" inserted")
cursor.execute("Select * from stud")
rows = cursor.fetchall()
print(rows)

cursor.execute("select * from stud where age between 18 and 25 ")
rows = cursor.fetchall()
print(rows)

# cursor.execute("Select * from stud where sid= ?",(1,))
# rows = cursor.fetchone()
# print(rows)
# cursor.execute("Delete from stud where sid = ?",(1,))
# cursor.execute("Select * from stud")
# rows = cursor.fetchall()
# print(rows)

