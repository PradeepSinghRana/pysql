import mysql.connector
y=mysql.connector.connect(
    host="localhost",
    user="pradeep",
    password="pradeep@1234", 
    database="pradeep"
)
mycursor=y.cursor()
#mycursor.execute("CREATE DATABASE pradeep")
mycursor.execute("SHOW DATABASES")
for db in mycursor:
    print(db)
mycursor.execute("CREATE TABLE students (name varchar(25),age varchar(10))")
mycursor.execute("SHOW TABLES")
for tb in mycursor:
    print(tb)
