from init import *
from HomePage import *

from PIL import ImageTk, Image

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
            l4.place(x= 150,y=300)
            signup_window.after(3000, signup_window.destroy)
            
        else:
            l4 = Label(signup_window, width = 30, text="Enter valid information!", background=label_colour, font=(myfont, 12, 'italic'))
            l4.place(x= 100,y=300)

    #create a new window for signup process
    signup_window = Tk() 
    signup_window.title("Sign Up") 
    signup_window.geometry("450x350")
    signup_window.configure(bg='#e1ddd7')

    greeting = Label(signup_window, text="Sign Up", pady=40, background=label_colour, font = (myfont, 20, 'bold'))
    greeting.pack() 
    
    name_text = StringVar() #declaring string variable for storing name and password
    l1 = Label(signup_window,text="Username:", font = (myfont, 14), background=label_colour)
    l1.place(x=90,y=100)
    e1 = Entry(signup_window,textvariable=name_text, font = (myfont, 12))
    e1.place(x=190,y=100)
    
    email_text = StringVar()
    l2 = Label(signup_window,text="Email:", font = (myfont, 14), background=label_colour)
    l2.place(x=90,y=160)
    e2 = Entry(signup_window,textvariable=email_text, font = (myfont, 12))
    e2.place(x=190,y=160)
    
    password_text = StringVar()
    l3 = Label(signup_window,text="Password:", font = (myfont, 14), background=label_colour)
    l3.place(x=90,y=220)
    e3 = Entry(signup_window,textvariable=password_text,show='*', font = (myfont, 12))
    e3.place(x=190,y=220)

    b = Button(signup_window,text="Sign Up", command=signup_database, font = (myfont, 12),bg = button_colour)
    b.place(x=215,y=260)

    signup_window.mainloop()

def login_database():
    login_query = "SELECT * FROM user WHERE uname=? AND password=?"
    global user
    user = e1.get()
    login_tuple = (user, e2.get())
    cur.execute(login_query, login_tuple)
    row = cur.fetchall()
    if row!=[]:
        start_window.destroy()
        home(user)  
    else:
        l3.config(text="Wrong email or password!")

#create window
start_window = Tk()
start_window.title("Log In") 
start_window.geometry("%dx%d" % (width, height))

#insert image
image = Image.open('D:\\New\\RPPOOP-Project\\main_wallpaper.png')
my_img = image.resize((width, height))

background_img = ImageTk.PhotoImage(my_img)
can = Canvas(start_window,width=width, height=height)

can.pack(expand="true", fill="both")
can.create_image(0,0,image=background_img, anchor = "nw")


title = Label(start_window, text="Expense Tracker",  background=label_colour, font = (myfont, 24, 'bold'))
title.place(x=900, y = 60)

greeting = Label(start_window, text="Login", background=label_colour, font = (myfont, 19, 'bold'))
greeting.place(x=950, y = 150)

email_text = StringVar() #stores string
l1 = Label(start_window,text="Username:", font = (myfont, 14), background=label_colour)
l1.place(x=950,y=200)
e1 = Entry(start_window, textvariable=email_text, font = (myfont, 12))
e1.place(x=950,y=235)

password_text = StringVar()
l2 = Label(start_window,text="Password:", font = (myfont, 14), background=label_colour)
l2.place(x=950,y=280)
e2 = Entry(start_window, textvariable = password_text, show='*', font = (myfont, 12))
e2.place(x=950,y=315)

b1 = Button(start_window, command=login_database, width = 15, text="Login", font = (myfont, 12),bg = button_colour)
b1.place(x=965,y=360)  

l3 = Label(start_window, font = (myfont, 12, 'italic'), background=label_colour)
l3.place(x=950,y=395)   

l4 = Label(text= 'Not an existing', font =(myfont, 11, 'italic'), background=label_colour)
l4.place(x= 945, y=430)

l5 = Label(text= 'user?', font =(myfont, 11, 'italic'), background=label_colour)
l5.place(x= 945, y = 450)

b2 = Button(start_window, command=signup, text="Sign Up", font = (myfont, 11),bg = button_colour)
b2.place(x=1050,y=436)  
start_window.mainloop()

conn.close()