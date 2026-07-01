from db import conn,cursor
def insert_emp():
    name = input("Enter yr name: ")
    sal = int(input("Enter yr sal"))
    query = "insert emp (name,sal) values (%s,%s)"
    values = (name,sal)
    cursor.execute(query,values)
    conn.commit()
    print("Data inserted")