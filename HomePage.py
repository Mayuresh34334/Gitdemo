from init import *
from graphs import * 

#on pressing 'add expense button':
def addExpense(userid):
    def add_database():
        cur.execute("""CREATE TABLE IF NOT EXISTS expenses(USERID INTEGER REFERENCES user(id), 
            DATE DATE, 
            AMOUNT REAL, 
            CATEGORY TEXT,
            MOP TEXT,
            NOTE TEXT)""")
        
        
        # convert to sql format
        date = datetime.datetime.strptime(cal.get_date(), "%m/%d/%y").strftime("%Y-%m-%d")
        amt= amt_entry.get()
        cat = cat_text.get()
        mop = mop_text.get()
        note = note_entry.get()
        exp_query = '''INSERT INTO expenses(USERID, DATE, AMOUNT, CATEGORY, MOP, NOTE)
        VALUES(?,?,?,?,?,?)'''
        exp_tuple = (userid, date, amt, cat, mop, note)
        cur.execute(exp_query, exp_tuple)
        row = cur.fetchone()

        if(row!=[] and cat and mop and amt_entry.get().isdigit()):
            l5 = Label(addexp_window, text="Added Successfully",bg = label_colour,font = (myfont, 12))
            l5.pack(pady = 10)
        else:
            l5 = Label(addexp_window, text="Please enter all values",bg = label_colour,font = (myfont, 12))
            l5.pack(pady = 5)

        conn.commit()
        
    addexp_window = Tk()
    addexp_window.title('Add Expense')
    addexp_window.geometry("400x600")
    addexp_window.configure(bg=label_colour)

    amt_text = DoubleVar()
    cat_text = StringVar()
    cat_list = ["Savings", "Insurance", "Travel", "Utilities", "Transport", "Food", "Medical", "Entertainment", "Miscellaneous"]
    cat_list.sort()
    cat_menu = OptionMenu(addexp_window,cat_text, *cat_list)
    cat_menu.configure(bg=button_colour)
    cat_text.set("")

    mop_text = StringVar()
    mop_list = ["Cash", "Card", "UPI"]
    mop_menu = OptionMenu(addexp_window,mop_text, *mop_list)
    mop_menu.configure(bg=button_colour)
    mop_text.set("")

    note_text = StringVar()
    date_label = Label(addexp_window, text="Date", bg = label_colour, font = (myfont, 12))
    cal = Calendar(addexp_window, selectmode = 'day')

    amt_label = Label(addexp_window, text="Amount",bg = label_colour,font = (myfont, 12))
    amt_entry = Entry(addexp_window, textvariable= amt_text, font = (myfont, 12))
    note_entry = Entry(addexp_window, textvariable= note_text, font = (myfont, 12))
    cat_label = Label(addexp_window, text="Category", bg=label_colour, font = (myfont, 12))
    mop_label = Label(addexp_window, text="Mode of Payment", bg=label_colour, font = (myfont, 12))
    note_label = Label(addexp_window, text="Note",bg = label_colour,font = (myfont, 12))
    b = Button(addexp_window,text="Add", command=add_database, font = (myfont, 12),bg = button_colour)

    date_label.pack(pady = 10)
    cal.pack()
    amt_label.pack(pady = 10)
    amt_entry.pack()
    cat_label.pack(pady = 10)
    cat_menu.pack()
    mop_label.pack(pady = 10)
    mop_menu.pack()
    note_label.pack(pady = 10)
    note_entry.pack()
    b.pack(pady = 10)

#on pressing 'set budget' button
def setBudget(userid):
    budget_window = Tk()
    budget_window.title('Budget set')
    budget_window.geometry("300x300")
    budget_window.configure(bg=label_colour)
    v1 = DoubleVar()
    
    def setDatabase():
        budget = budget_entry.get()
        cat = cat_text.get()
        
        if(budget.isdigit() and cat):
            #userid amount category
            cur.execute("SELECT * FROM budget WHERE CATEGORY = ?", (cat,))
            result = cur.fetchall()
            if(result == []):
                exp_query = '''INSERT INTO budget(USERID, AMOUNT, CATEGORY)
                    VALUES(?,?,?)'''
                exp_tuple = (userid, budget, cat)
                cur.execute(exp_query, exp_tuple)
            else:
                cur.execute("UPDATE budget SET amount = ? WHERE category = ?", (budget, cat))

            l1 = Label(budget_window,text = "Budget set successfully!" ,bg = label_colour)
            l1.pack()
        else:
            print("Please try again")
            l1 = Label(budget_window,text = "Invalid" ,bg = label_colour)
            l1.pack()

        conn.commit()
    cat_text = StringVar()
    cat_list = ["Savings", "Insurance", "Travel", "Utilities", "Transport", "Food", "Medical", "Entertainment", "Miscellaneous"]
    cat_list.sort()
    cat_menu = OptionMenu(budget_window,cat_text, *cat_list)
    cat_menu.configure(bg=button_colour)
    cat_text.set("")
    budget_entry = Entry(budget_window, bg = button_colour, font = (myfont, 12))

    #s1 = Scale( budget_window, variable = v1, from_ = 1, to = 10000, orient = HORIZONTAL)   
    budget_button = Button(budget_window, text = "Set", command=setDatabase, bg = button_colour, font = (myfont, 12))
    cat_label = Label(budget_window, text="Select category", bg=label_colour, font = (myfont, 12))
    cat_label.pack(pady = 10)
    
    #s1.pack() 
    cat_label.pack()
    cat_menu.pack()
    budget_entry.pack(pady = 10)
    budget_button.pack(pady = 10) 
    budget_window.mainloop()

def home(user):
    #table creation
    cur.execute('''CREATE TABLE IF NOT EXISTS expenses(USERID INTEGER REFERENCES user(id), 
    DATE DATE, 
    AMOUNT REAL, 
    CATEGORY TEXT,
    MOP TEXT,
    NOTE TEXT)''')

    #window creation
    home_window = Tk()
    home_window.title('Home')
    home_window.geometry("%dx%d" % (width, height))
    home_window.configure(bg=label_colour)

    cur.execute("SELECT ID FROM USER WHERE UNAME = ?", (user,))
    userid = cur.fetchone()[0]

    button1 = Button(home_window,text="Add Expenses",width=20, command=lambda: addExpense(userid), bg = button_colour, font = (myfont, 12))
    button1.pack(pady=30)

    button2 = Button(home_window,text="View Graphs",width=20, command = lambda: viewGraph(userid), bg = button_colour, font = (myfont, 12))
    button2.pack(pady=30)

    button3 =  Button(home_window, text="Set budget",width=20, command= lambda: setBudget(userid), bg = button_colour, font = (myfont, 12))
    button3.pack(pady = 30)

    button4 =  Button(home_window, text="View Expenses",width=20, command= lambda: viewTable(userid), bg = button_colour, font = (myfont, 12))
    button4.pack(pady = 30)

    home_window.mainloop()