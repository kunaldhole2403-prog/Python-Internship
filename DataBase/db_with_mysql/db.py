import mysql.connector
#con create
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Kunal@123",
    database="linkcode"
)
print("database created")
cursor=conn.cursor()
cursor.execute("""
    create table if not exists emp(
               empid int primary key auto_increment,
               name varchar(20) not null,
               sal decimal(10,2) check(sal>0)
               )
""")
conn.commit()
print("table created")