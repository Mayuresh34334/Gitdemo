import mysql.connector

#connecting mysql and python
try:
  conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "MySQLShell23",
    database = "ExpenseTracker"
  )
except:
   print("Unable to connect to database")
   
cur = conn.cursor()
print(conn)

cur.execute('''SELECT * FROM USER;''')
for x in cur:
    print(x)

"""
cur.execute('''CREATE TABLE USER (ID INT PRIMARY KEY NOT NULL,
         UNAME TEXT NOT NULL,
        EMAIL TEXT NOT NULL,
        PWD TEXT NOT NULL);''')

cur.execute('''insert into user(id, uname, email, pwd) values(3, 'a', 'a@mail.com', '43q1')''')
"""

uname=input('Username: ')
email=input('Email: ')
pwd = input('Password: ')

user_query = '''insert into user(id, uname, email, pwd) values(%s,%s,%s,%s)'''
user_tup = (4, uname, email, pwd)
cur.execute(user_query,user_tup)
conn.commit()
cur.close()