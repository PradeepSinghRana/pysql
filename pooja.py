import mysql.connector
x=mysql.connector.connect(host="localhost",
                          user="root",
                          password="pradeep@1234",
                          database="pooja")
cursor=x.cursor()
#cursor.execute("CREATE TABLE table1(name varchar(20),address varchar(20))")
cursor.execute("insert into table1 values('pinky','kaithal'),('ishan','allsoft'),('pinky','kaithal')")
x.commit()
print(cursor.rowcount,"row inserted")
cursor.execute("SELECT * FROM table1")
y=cursor.fetchall()

for z in y:
    print(z)




