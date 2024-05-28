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
# query = "select * from students where id in (1,3,5)" 
# query = "select * from students where id between 2 and 4" 
# query = "select * from students where name like 'r%' and id=2" 
# query = "select * from students where name like '%i' " 
# query = "select * from students where name like '%a%' " 
# query = "select * from students where name like '__v%' " 
query = "select * from students" 
cursor.execute(query)
res = cursor.fetchall()
for i in res:
    print(i)