import sqlite3
conn = sqlite3.connect("student.db")
cursor = conn.cursor()

cursor.execute("""
        create table if not exists Result(
               sid integer primary key,
               sname text not null,
               dcn integer not null,
               java integer not null,
               mic integer not null
               )
""")

def add():
    sid = int(input("Enter Your Id: "))
    name = input("Enetr your name: ")
    dcn = int(input("Enter your DCN marks: "))
    java = int(input("Enter your JAVA marks: "))
    mic = int(input("Enter your MIC marks: "))
    try:
        cursor.execute("insert into Result (sid, sname, dcn, java, mic) VALUES (?,?,?,?,?)",(sid,name,dcn,java,mic))
        conn.commit()
        print("Data Is Inserted Successfully")
        print("-"*80)
    except Exception as e:
        print(e)
        print("-"*80)
def update():
    upch = 0
    while upch!= 5:
        print("1.Update Name\n2.Update DCN Marks\n3.Update Java Marks\n4.Update MIC marks:")
        upch = int(input("Enter your update choice: "))
        try:
            match upch:
                case 1:
                    upid = int(input("Enetr Your Id: "))
                    newname = input("Enter New Name: ")
                    cursor.execute("Update Result set sname = ? where sid = ?",(newname,upid))
                    if cursor.rowcount > 0:
                        conn.commit()
                        print("Data Updated Successfully")
                        print("-"*80)
                    else:
                        print("Student ID Not Found")
                        print("-"*80)
                case 2:
                    upid = int(input("Enetr Your Id: "))
                    newdcn = int(input("Enter New DCN Marks: "))
                    cursor.execute("Update Result set dcn = ? where sid = ?",(newdcn,upid))
                    if cursor.rowcount > 0:
                        conn.commit()
                        print("Data Is Updated successfully")
                        print("-"*80)
                    else:
                        print("Data is not Found")
                        print("-"*80)
                case 3:
                    upid = int(input("Enetr Your Id: "))
                    newjava = int(input("Enter New Java Marks: "))
                    cursor.execute("Update Result set java = ? where sid = ?",(newjava,upid))
                    if cursor.rowcount > 0:
                        conn.commit()
                        print("Data Is Updated successfully")
                        print("-"*80)
                    else:
                        print("Data is not Found")
                        print("-"*80)
                case 4:
                    upid = int(input("Enetr Your Id: "))
                    newmic = int(input("Enter New Mic Marks: "))
                    cursor.execute("Update Result set mic = ? where sid = ?",(newmic,upid))
                    if cursor.rowcount > 0:
                        conn.commit()
                        print("Data Is Updated successfully")
                        print("-"*80)
                    else:
                        print("Data is not Found")
                        print("-"*80)
                case 5:
                    print("Returning to main menu...")
                    print("-"*80)
                case _:
                    print("Invalid Update Choice!")
                    print("-"*80)
        except Exception as e:
            print(e)
def read():
    print("Id\tName\tDCN\tJAVA\tMIC")
    cursor.execute("Select * from Result")
    data = cursor.fetchall()
    for row in data:
        print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}")
    if not data:
        print("No Record Found")
    print("-"*80)

def search():
    sid = int(input("Enter The Id to Search: "))

    cursor.execute("SELECT * FROM Result WHERE sid = ?", (sid,))
    data = cursor.fetchone()

    if data:
        print(f"ID:{data[0]}\tName:{data[1]}\tDCN:{data[2]}\tJAVA:{data[3]}\tMIC:{data[4]}")
    else:
        print("Student ID Not Found")

    print("-" * 80)

def delete():
    dch = 0
    while dch!= 3:
        print("1.Delete a row\t2.Delete all data\t3.Return to main manu4")
        dch = int(input("Enter a choice: "))
        match dch:
            case 1 :
                sid = int(input("Enter the ID: "))
                cursor.execute("delete from result where sid = ?",(sid,))
                if cursor.rowcount > 0:
                    conn.commit()
                    print("Row Deleted Successfully")
                    print("-"*80)
                else:
                    print("Student ID Not Found")
                    print("-"*80)
            case 2:
                cursor.execute("delete from Result")
                conn.commit()
                print("All DA Deleted Successfully")
                print("-"*80)
            case 3:
                print("Returing to menu")
                print("-"*80)
            case _:
                print("Invalid Choice")
                print("-"*80)
def viewRes():
    print("ID\tName\tDCN\tJAVA\tMIC\tTotal\tPercentage")
    cursor.execute("Select * from Result")
    data = cursor.fetchall()
    for row in data:
        total = row[2] + row[3] + row[4]
        percentage = (total / 300) * 100
        print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}\t{total}\t{percentage:.2f}%")
    if not data:
        print("No Record Found")
    print("-"*80)

def genReport():
    
    cursor.execute("Select * from Result")
    data = cursor.fetchall()
    print("Pass Student:\n")
    print("ID\tName\tDCN\tJAVA\tMIC\tTotal\tPercentage")
    for row in data:
        total = row[2] + row[3] + row[4]
        percentage = (total / 300) * 100
        if percentage >= 40:
            print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}\t{total}\t{percentage:.2f}%")
    print("-"*80)
    print("Fail Student:\n")
    print("ID\tName\tDCN\tJAVA\tMIC\tTotal\tPercentage")
    for row in data:
        total = row[2] + row[3] + row[4]
        percentage = (total / 300) * 100
        if percentage < 40:
            print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}\t{total}\t{percentage:.2f}%")
    print("-"*80)

ch = 0
while ch!= 8:
    print("1.Add Data\n2.Update Data\n3.Read Data\n4.Search Data\n5.Delete Data\n6.View Result\n7.Generate report\n8.EXIT")
    ch = int(input("Enter you choice: "))
    match ch:
        case 1:
            print("-"*80)
            add()
        case 2:
            print("-"*80)
            update()
        case 3:
            print("-"*80)
            read()
        case 4:
            print("-"*80)
            search()
        case 5:
            print("-"*80)
            delete()
        case 6:
            print("-"*80)
            viewRes()
        case 7:
            genReport()
        case 8:
            exit()
        case _:
            print("Inavalid Choice")