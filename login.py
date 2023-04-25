from tkinter import *
import mysql.connector
import sqlite3
#import seaborn as sns

#create an object to create a window
window = Tk()
window.title('Registration')
window.geometry("550x350")
window.configure(bg='#CDF0EA')
myfont = ('Inter')

#connecting to database
try:
    conn = sqlite3.connect('ExpenseTracker.db')
    cur = conn.cursor()
    print("Successfully connected to database")
except:
    print("Unable to connect to database")
    
"""
conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "MySQLShell23",
        database = "ExpenseTracker"
    )
cur = conn.cursor()
"""

#Actions on Pressing Login Button
def login():
    def login_database():
        login_query = "SELECT * FROM test WHERE email=%s AND password=%s"
        login_tuple = (e1.get(), e2.get())
        cur.execute(login_query, login_tuple)
        row = cur.fetchall()
        print(row)
        if row!=[]:
            #proceed to main window
            l3.config(text="User found")
        else:
            l3.config(text="Wrong email or password!")

    window.destroy()  #close the previous window

    #create a new window for loging in
    login_window = Tk()
    login_window.title("Log In") 
    login_window.geometry("550x350")
    login_window.configure(bg='#D2DAFF')
    greeting = Label(login_window, text="Login", pady=40, background="#D2DAFF", font = (myfont, 20, 'bold'))
    greeting.pack()

    l1 = Label(login_window,text="Email:", font = (myfont, 14), background="#D2DAFF")
    l1.place(x=125,y=100)
    email_text = StringVar() #stores string
    e1 = Entry(login_window, textvariable=email_text, font = (myfont, 12))
    e1.place(x=220,y=100)
    
    l2 = Label(login_window,text="Password:", font = (myfont, 14), background="#D2DAFF")
    l2.place(x=125,y=160)
    password_text = StringVar()
    e2 = Entry(login_window, textvariable = password_text, show='*', font = (myfont, 12))
    e2.place(x=220,y=160)
    
    b = Button(login_window, command=login_database, text="Login", font = (myfont, 12),bg = '#F3F8FF')
    b.place(x=250,y=200)
    
    l3 = Label(login_window, font = (myfont, 12, 'italic'), background="#D2DAFF")
    l3.place(x=180,y=250)

    login_window.mainloop()

#Actions on Pressing Signup button
def signup():
    #creates database to store user details
    def signup_database():
        if(e1.get().strip() != '' and  e2.get().strip() != '' and e3.get().strip() != ''):
            cur.execute("CREATE TABLE IF NOT EXISTS test(ID INT PRIMARY KEY AUTO_INCREMENT,name text,email text,password text)")
            user_query = '''insert into test(name, email, password) values(%s,%s,%s)'''
            user_tup = (e1.get(), e2.get(), e3.get())
            cur.execute(user_query,user_tup)
            conn.commit()  

            l4 = Label(signup_window,text="Account created successfully!", background="#D2DAFF", font=(myfont, 12, 'italic'))
            l4.place(x= 170,y=300)
            
        else:
            l4 = Label(signup_window, width = 30, text="Enter valid information!", background="#D2DAFF", font=(myfont, 12, 'italic'))
            l4.place(x= 150,y=300)

    window.destroy()  #close the previous window

    #create a new window for signup process
    signup_window = Tk() 
    signup_window.title("Sign Up") 
    signup_window.geometry("550x370") 
    signup_window.configure(bg='#D2DAFF')

    greeting = Label(signup_window, text="Sign Up", pady=40, background="#D2DAFF", font = (myfont, 20, 'bold'))
    greeting.pack() 

    l1 = Label(signup_window,text="Username:", font = (myfont, 14), background="#D2DAFF")
    l1.place(x=125,y=100)
    name_text = StringVar() #declaring string variable for storing name and password
    e1 = Entry(signup_window,textvariable=name_text, font = (myfont, 12))
    e1.place(x=225,y=100)

    l2 = Label(signup_window,text="Email:", font = (myfont, 14), background="#D2DAFF")
    l2.place(x=125,y=160)
    email_text = StringVar()
    e2 = Entry(signup_window,textvariable=email_text, font = (myfont, 12))
    e2.place(x=225,y=160)

    l3 = Label(signup_window,text="Password:", font = (myfont, 14), background="#D2DAFF")
    l3.place(x=125,y=220)
    password_text = StringVar()
    e3 = Entry(signup_window,textvariable=password_text,show='*', font = (myfont, 12))
    e3.place(x=225,y=220)

    b = Button(signup_window,text="signup", command=signup_database, font = (myfont, 12),bg = '#F3F8FF')
    b.place(x=250,y=260)

    signup_window.mainloop()

greeting = Label(window, text="Personal Finance Tracker", pady=40, background="#CDF0EA", font = (myfont, 20, 'bold'))
greeting.pack()
button1 = Button(window, text="Login",width=20, command=login, bg = '#F3F8FF', font = (myfont, 12))
button1.pack(pady=15)
button2 = Button(window,text="Signup",width=20, command=signup, bg = '#F3F8FF', font = (myfont, 12))
button2.pack(padx=5, pady=15)
window.mainloop()
conn.close() 