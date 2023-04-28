from tkinter import *
import sqlite3

#connecting to database
try:
    conn = sqlite3.connect('Project/ExpenseTracker.db') #database path
    cur = conn.cursor()
except:
    print("Unable to connect to database")


def main():
    def login_database():
        login_query = "SELECT * FROM user WHERE uname=? AND password=?"
        global user
        user = e1.get()
        login_tuple = (user, e2.get())
        cur.execute(login_query, login_tuple)
        row = cur.fetchall()
        #print(row)
        if row!=[]:
            home()
        else:
            l3.config(text="Wrong email or password!")
    
    login_window = Tk()
    login_window.title("Log In") 
    global width, height, myfont
    width= login_window.winfo_screenwidth()               
    height= login_window.winfo_screenheight()   
    myfont = ('Inter')

    login_window.geometry("%dx%d" % (width, height))
    login_window.configure(bg='#D2DAFF')
    greeting = Label(login_window, text="Login", pady=40, background="#D2DAFF", font = (myfont, 20, 'bold'))
    greeting.pack()

    email_text = StringVar() #stores string
    l1 = Label(login_window,text="Email:", font = (myfont, 14), background="#D2DAFF")
    l1.pack(pady=10)
    e1 = Entry(login_window, textvariable=email_text, font = (myfont, 12))
    e1.pack()
    
    password_text = StringVar()
    l2 = Label(login_window,text="Password:", font = (myfont, 14), background="#D2DAFF")
    l2.pack(pady = 10)
    e2 = Entry(login_window, textvariable = password_text, show='*', font = (myfont, 12))
    e2.pack()

    l3 = Label(login_window, font = (myfont, 12, 'italic'), background="#D2DAFF")
    l3.pack(pady=5)

    b = Button(login_window, command=login_database, text="Login", font = (myfont, 12),bg = '#F3F8FF')
    b.pack(pady=10)

    login_window.mainloop()
    
#Actions on Pressing Signup button
def signup():
    #creates database to store user details
    def signup_database():
        if(e1.get().strip() != '' and  e2.get().strip() != '' and e3.get().strip() != ''):
            cur.execute("CREATE TABLE IF NOT EXISTS user(ID INTEGER PRIMARY KEY AUTOINCREMENT,uname text,email text,password text)")
            user_query = '''insert into user(uname, email, password) values(?,?,?)'''
            user_tup = (e1.get(), e2.get(), e3.get())
            cur.execute(user_query,user_tup)
            conn.commit()  

            l4 = Label(signup_window,text="Account created successfully!", background="#D2DAFF", font=(myfont, 12, 'italic'))
            l4.place(x= 170,y=300)
            
        else:
            l4 = Label(signup_window, width = 30, text="Enter valid information!", background="#D2DAFF", font=(myfont, 12, 'italic'))
            l4.place(x= 150,y=300)

    #create a new window for signup process
    signup_window = Tk() 
    signup_window.title("Sign Up") 
    signup_window.geometry("%dx%d" % (width, height))
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
    b.pack(pady=10)

    signup_window.mainloop()
    
    
def home():
    #table creation
    cur.execute('''CREATE TABLE IF NOT EXISTS expenses(SNO INTEGER PRIMARY KEY AUTOINCREMENT, 
        USERID INTEGER REFERENCES user(id), 
        DATE DATE, 
        AMOUNT REAL, 
        CATEGORY TEXT,
        MOP TEXT,
        NOTE TEXT)''')

    home_window = Tk()
    home_window.title('Registration')
    home_window.geometry("%dx%d" % (width, height))
    home_window.configure(bg='#CDF0EA')
 
    def addExpense(username):
        date = input('Date (yyyy-mm-dd):')
        amt = float(input('Amt:'))
        cat = input('Category:')
        mop = input('Cash/UPI/Card: ')
        note = input('Note:')
        
        cur.execute("SELECT ID FROM USER WHERE UNAME = ?", (username,))
        userid = cur.fetchone()[0]
        
        exp_query = '''INSERT INTO expenses(USERID, DATE, AMOUNT, CATEGORY, MOP, NOTE)
        VALUES(?,?,?,?,?,?)'''
        exp_tuple = (userid, date, amt, cat, mop, note)
        cur.execute(exp_query, exp_tuple)
        conn.commit()
    
    #budget setting
    #on pressing 'add expense button':
    button2 = Button(home_window,text="+",width=20, command=lambda: addExpense(user), bg = '#F3F8FF', font = (myfont, 12))
    button2.pack(padx=5, pady=15)

    home_window.mainloop()

if __name__ == "__main__":
    main()
conn.close()