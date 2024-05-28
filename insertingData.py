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
query = "insert into students (id,name,marks) values (%s,%s,%s)" 
values = ((8,"Vinish",20),(9,"Ekta",15))
# for i in values:
#     cursor.execute(query,i)
cursor.executemany(query,values)
conn.commit()