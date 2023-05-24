from init import *
from excel import *

def viewGraph(userid):
    def view_pie():
        month_selected = month_text.get()
        pie_query = '''SELECT category, ROUND(SUM(amount),2) 
            FROM expenses 
            WHERE strftime('%m', date)= ?  AND userid = ?
            GROUP BY category'''
        cur.execute(pie_query, (month_selected, userid))
        Amounts = []
        Categories = []

        result = cur.fetchall()
        for i in result:
            Amounts.append(i[1])
            Categories.append(i[0])

        # Visualize Data
        y = np.array(Amounts)
        plt.pie(y, labels=Categories)
        #plt.title("{}'s Expenses by Categories".format('March'))
        plt.legend(title="Categories:")
        plt.show()

    def view_bar():
        month_selected = month_text.get()

        bar_query = '''SELECT category, ROUND(SUM(amount),2) 
            FROM expenses 
            WHERE strftime('%m', date)= ? AND userid = ?
            GROUP BY category'''
        cur.execute(bar_query,(month_selected, userid))

        result = cur.fetchall()

        Amounts = []
        Categories = []
        for i in result:
            Amounts.append(i[1])
            Categories.append(i[0])
        # Visualize Data
        plt.bar(Categories, Amounts)
        plt.xlabel("Categories")
        plt.ylabel("Amount (₹)")
        #plt.title("{}'s Expenses".format('March'))
        plt.show()

    graph_window = Tk()
    graph_window.title('Graphs')
    graph_window.geometry("300x300")
    graph_window.configure(bg=label_colour)

    month_label = Label(graph_window, text="Select month:", bg = label_colour, font = (myfont, 12))
    month_text = StringVar()
    month_list = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
    month_menu = OptionMenu(graph_window, month_text, *month_list)
    month_menu.configure(bg=button_colour)
    month_text.set("")
        
    bar_button = Button(graph_window,text="Bar Graph",width=20, command=view_bar, bg = button_colour, font = (myfont, 12))
    pie_button = Button(graph_window,text="Pie Chart",width=20, command=view_pie, bg = button_colour, font = (myfont, 12))
    month_label.pack(pady=15)
    month_menu.pack()
    bar_button.pack(pady=15)
    pie_button.pack(pady=15)

def viewTable(userid):
    def showFig():
        month_selected = month_text.get()
        pie_query = '''SELECT * FROM expenses 
            WHERE strftime('%m', date)= ?  AND userid = ?'''
        cur.execute(pie_query, (month_selected, userid))
        result = cur.fetchall()
        Amounts = []
        Categories = []
        Dates = []
        #(1, '2023-03-21', 3000.0, 'Travel', 'UPI', 'Petrol')
        for i in result:
            Dates.append(i[1])
            Amounts.append(i[2])
            Categories.append(i[3])

        fig = go.Figure(data=[go.Table(header=dict(values=["Date", "Amount", "Category"]),
                                    cells=dict(values=[Dates, Amounts, Categories]))])
        #fig.update_layout(title_text=month_selected + "'s Expenses", title_x=0.5)
        fig.show()

    table_window = Tk()
    table_window.title('Table')
    table_window.geometry("300x300")
    table_window.configure(bg=label_colour)

    month_label = Label(table_window, text="Select month:", bg = label_colour, font = (myfont, 12))
    month_text = StringVar()
    month_list = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
    month_menu = OptionMenu(table_window, month_text, *month_list)
    month_menu.configure(bg=button_colour)
    month_text.set("")
    month_label.pack(pady=15)
    month_menu.pack()

    label = Label(table_window, text = 'View as table:', bg = label_colour, font = (myfont, 11, 'italic'))
    label.pack(pady = 10)
    b = Button(table_window, text="View",width=20, command= showFig, bg = button_colour, font = (myfont, 12))
    b.pack(pady = 10)

    label = Label(table_window, text = 'Export to excel:', bg = label_colour, font = (myfont, 11, 'italic'))
    label.pack(pady = 10)
    b2 = Button(table_window, text="Excel",width=20, command= lambda:  export(userid), bg = button_colour, font = (myfont, 12))
    b2.pack()