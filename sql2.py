import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="pradeep",
    password="pradeep@1234",
    database="pradeep"
)
mycursor=mydb.cursor()
sqlFormula="INSERT INTO students(name,age) VALUES(%s,%s)"
students=[("pradeep",20),
          ("ram",24),
          ("pspsam", 23),
          ("shankar", 30),
          ("raghav",20),
          ("pooja",20),
          ("apapap",12),
          ("vneet",23),
          ("manoj",10),
          ("manish",13)
    ]
mycursor.executemany(sqlFormula,students)
mydb.commit()
#mycursor.execute("SELECT*FROM students")
#myresult=mycursor.fetchall()
#for z in myresult:
#    print(z)

mycursor.execute("SELECT age FROM students")
myresult=mycursor.fetchall()

for age in myresult:
    print(age)

mycursor.execute("SELECT*FROM students  WHERE age=20")
myresult=mycursor.fetchall()
for x in myresult:
    print(x)

mycursor.execute("SELECT*FROM students  WHERE age LIKE '%0%'")
myresult=mycursor.fetchall()
for x in myresult:
    print(x)

