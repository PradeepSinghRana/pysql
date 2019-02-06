import mysql.connector
x=mysql.connector.connect(host="localhost",
                          user="pradeep",
                          password="pradeep@1234",
                          database="allsoft")
cursor=x.cursor()
#cursor.execute("CREATE TABLE table2(name varchar(255),address varchar(255))")
cursor.execute("insert into table2 values('pradeep','almora'),('pooooojajajajjaja','nepal')")
x.commit()
print(cursor.rowcount)
cursor.execute("SELECT*FROM table2")
myresult=cursor.fetchall()
for y in myresult:
    print(y)

