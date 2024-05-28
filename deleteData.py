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
cursor = conn.cursor()
# query = "delete from students where id=1 "
query = "update students set marks = 0 where id = 1"
cursor.execute(query)
conn.commit()