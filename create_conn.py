import mysql.connector
# username,
#host
#password
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    # password="root"
)
print(conn)
# it will help in query executions
cursor = conn.cursor()
# query = "create database school"
query = "show databases"
cursor.execute(query)
for i in cursor:
    print(i)


