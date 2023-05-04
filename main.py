from tkinter import *
import sqlite3
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import numpy as np

#connecting to database
#try:
conn = sqlite3.connect('ExpenseTracker.db') #database path
cur = conn.cursor()
#except:
 #   print("Unable to connect to database")


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

    #insert image
    image=Image.open('main_wallpaper.png')
    my_img = image.resize((width, height))
    background_img = ImageTk.PhotoImage(my_img)
    can = Canvas(login_window,width=width, height=height)
    can.pack(expand="true", fill="both")
    can.create_image(0,0,image=background_img, anchor = "nw")

    #create window
    login_window.geometry("%dx%d" % (width, height))
    #login_window.configure(bg='#D2DAFF')
    label_colour = "#e1ddd7"
    button_colour = "#f9f6f6"
    title = Label(login_window, text="Expense Tracker",  background=label_colour, font = (myfont, 24, 'bold'))
    title.place(x=900, y = 60)

    greeting = Label(login_window, text="Login", background=label_colour, font = (myfont, 19, 'bold'))
    greeting.place(x=950, y = 150)

    email_text = StringVar() #stores string
    l1 = Label(login_window,text="Username:", font = (myfont, 14), background=label_colour)
    l1.place(x=950,y=200)
    e1 = Entry(login_window, textvariable=email_text, font = (myfont, 12))
    e1.place(x=950,y=235)
    
    password_text = StringVar()
    l2 = Label(login_window,text="Password:", font = (myfont, 14), background=label_colour)
    l2.place(x=950,y=280)
    e2 = Entry(login_window, textvariable = password_text, show='*', font = (myfont, 12))
    e2.place(x=950,y=315)
    
    b1 = Button(login_window, command=login_database, width = 15, text="Login", font = (myfont, 12),bg = button_colour)
    b1.place(x=965,y=360)  
    
    l3 = Label(login_window, font = (myfont, 12, 'italic'), background=label_colour)
    l3.place(x=950,y=395)   

    l4 = Label(text= 'Not an existing', font =(myfont, 11, 'italic'), background=label_colour)
    l4.place(x= 945, y=430)

    l5 = Label(text= 'user?', font =(myfont, 11, 'italic'), background=label_colour)
    l5.place(x= 945, y = 450)

    b2 = Button(login_window, command=signup, text="Sign Up", font = (myfont, 11),bg = button_colour)
    b2.place(x=1050,y=436)  
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

            l4 = Label(signup_window,text="Account created successfully!", background=label_colour, font=(myfont, 12, 'italic'))
            l4.place(x= 170,y=300)
            
        else:
            l4 = Label(signup_window, width = 30, text="Enter valid information!", background=label_colour, font=(myfont, 12, 'italic'))
            l4.place(x= 150,y=300)

    #create a new window for signup process
    signup_window = Tk() 
    signup_window.title("Sign Up") 
    signup_window.geometry("450x350")
    signup_window.configure(bg='#e1ddd7')

    label_colour = "#e1ddd7"
    button_colour = "#f9f6f6"

    greeting = Label(signup_window, text="Sign Up", pady=40, background=label_colour, font = (myfont, 20, 'bold'))
    greeting.pack() 
    
    name_text = StringVar() #declaring string variable for storing name and password
    l1 = Label(signup_window,text="Username:", font = (myfont, 14), background=label_colour)
    l1.place(x=100,y=100)
    e1 = Entry(signup_window,textvariable=name_text, font = (myfont, 12))
    e1.place(x=200,y=100)
    
    email_text = StringVar()
    l2 = Label(signup_window,text="Email:", font = (myfont, 14), background=label_colour)
    l2.place(x=100,y=160)
    e2 = Entry(signup_window,textvariable=email_text, font = (myfont, 12))
    e2.place(x=200,y=160)
    
    password_text = StringVar()
    l3 = Label(signup_window,text="Password:", font = (myfont, 14), background=label_colour)
    l3.place(x=100,y=220)
    e3 = Entry(signup_window,textvariable=password_text,show='*', font = (myfont, 12))
    e3.place(x=200,y=220)

    b = Button(signup_window,text="Sign Up", command=signup_database, font = (myfont, 12),bg = button_colour)
    b.place(x=225,y=260)

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
    home_window.configure(bg='#dcd3e1')
 
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

def view_bar(month_selected):
    bar_query = '''SELECT category, ROUND(SUM(amount),2) 
        FROM expenses 
        WHERE strftime('%m', date)= ? 
        GROUP BY category'''
    cur.execute(bar_query,(month_selected,))

    result = cur.fetchall()
    Amounts = []
    Categories = []
    for i in result:
        # Names.append(i[0])
        Amounts.append(i[1])
        Categories.append(i[0])

    # Visualize Data
    plt.bar(Categories, Amounts)
    plt.xlabel("Categories")
    plt.ylabel("Amount (₹)")
    #plt.title("{}'s Expenses".format('March'))
    plt.show()

def view_pie(month_selected):
    pie_query = '''SELECT category, ROUND(SUM(amount),2) 
        FROM expenses 
        WHERE strftime('%m', date)= ?  
        GROUP BY category'''
    cur.execute(pie_query, (month_selected,))
    result = cur.fetchall()
    Amounts = []
    Categories = []
    for i in result:
        Categories.append(i[0])
        Amounts.append(i[1])

    # Visualize Data
    y = np.array(Amounts)
    my_labels = Categories
    plt.pie(y, labels=my_labels)
    plt.title("{}'s Expenses by Categories".format('March'))
    plt.legend(title="Categories:")
    plt.show()

view_pie('03')
"""
if __name__ == "__main__":
    main()
"""
conn.close()
