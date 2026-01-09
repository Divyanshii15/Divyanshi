# import mysql.connector

#establish connection to mysql

# connection=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="root",
#     database="Connection"
# )

# if connection.is_connected():
#     print("connection Successful")
# else:
#     print("Connection Failed")

    #create a DATABASE 

# cursor=connection.cursor()

# cursor.execute("create database Connection ")
# print("Database connected to Python")

# connection.close()


# cursor=connection.cursor()

# cursor.execute("create table Students (id int, name varchar(20), age int, gender varchar(10))")
# print("Table Created Successfully")
# cursor.execute("""insert into Students
#                values(1,'divi',20,'female'),
#                (2,'shakshi',24,'Female'),
#                (3,'aman',22,'male')
#                """)


# print("insert successfull")
# connection.commit()
# connection.close()

###############################################################################

# import mysql.connector

# connection=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="root",
#     database="Connection"
# )

# cursor=connection.cursor()

# cursor.execute("""create table stdmarks(
#                id int auto_increment primary key,
#                name varchar(20),
#                age int,
#                marks int,
#                course varchar(20)
#                )""")
# print("table created Succesfully")

# connection.close()

#insert data

# std=[("divi",20,99,"AIPA"),
#     ("shakshi",22,66, "COPA"),
#     ("vidhya",21,58,"CSA"),
#     ]
# query="insert into stdmarks (name, age, marks , course) value (%s,%s,%s,%s)"
# cursor.executemany(query, std)
# connection.commit()
# print("Data Insered Successfully")

# connection.close()

         #read data

# cursor.execute("select * from stdmarks")
# cursor.execute("select name, cursor from stdmarks")
# abc=cursor.fetchall()
# for i in abc:
#     print(i)


          #update data

# cursor.execute("update stdmarks set marks=95 where id =1")
# connection.commit()
# print("data updated successfully")


# cursor.execute("delete from stdmarks where name='shakshi'")

# connection.commit()
# print("Deleted Successfully") 

# connection.close()

# import mysql.connector

# connection=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="root",
#     database="Connection"
# )

# cursor=connection.cursor()
# cursor.execute("""create table Details(
#                id int auto_increment primary key,
#                name varchar (20_),
#                age int, 
#                marks int,
#                course varchar(20)
#                )""")
# print("Table Created Successfully")








import mysql.connector

library=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
    # database="library"
)

if library.is_connected():
    print("connection  Successful")
else:
    print("Connection Failed")

# cursor=library.cursor()
# cursor.execute("""create table Book(
#                book_id int primary key auto_increment ,
#                author varchar(20),
#                title varchar(20)
#                )""")

# print("successful")


# cursor=library.cursor()
# cursor.execute("select * from ")