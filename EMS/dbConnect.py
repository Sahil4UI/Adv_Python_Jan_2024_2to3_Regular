import mysql.connector
# username,
#host
#password
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    database= "employee",
)

# it will help in query executions
cursor = conn.cursor()
# query = "create database school"

cursor.execute("show tables")
tables = []
for i in cursor:
    tables.append(i[0])

if "emp_record" not in tables:
    query = '''create table emp_record(
    id int primary key auto_increment,
    department text,
            designation text,
            address text,
            date_of_birth text,
            name Text,
            email Text,
            married_status Text,
            date_of_joining Text,
            gender Text,
            phone_number Text,
            country Text,
            salary int)'''
    cursor.execute(query)


def appendData(dataList):
    data = list(dataList.values())
    query = '''insert into emp_record (department,
            designation,
            address,
            date_of_birth,
            name,
            email,
            married_status,
            date_of_joining,
            gender,
            phone_number,
            country,
            salary )
            values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) '''
    cursor.execute(query,data)

def loadData():
    cursor.execute("select * from emp_record")
    d = []
    for i in cursor.fetchall():
        d.append(i)
    return d



