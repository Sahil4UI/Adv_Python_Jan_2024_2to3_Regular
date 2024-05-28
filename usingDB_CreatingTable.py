import mysql.connector
# username,
#host
#password
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    database = "school"
    # password="root"
)
print(conn)
# it will help in query executions
cursor = conn.cursor()
# query  = "create table students(id int primary key,name text,marks int)"
query = "show tables"
cursor.execute(query)
for i in cursor:
    print(i)