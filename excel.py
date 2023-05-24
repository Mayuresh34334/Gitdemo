from init import *
import openpyxl

def export(userid):
  def createExcel():
    book = openpyxl.Workbook()
    sheet = book.active

    cur.execute("SELECT * FROM `expenses` where userid = ?", (userid,))
    results = cur.fetchall()
    i = 0
    for row in results:
      i += 1
      j = 1
      for col in row:
        cell = sheet.cell(row = i, column = j)
        cell.value = col
        j += 1
    
    fname= ex_entry.get()
    book.save(fname + ".xlsx")

  ex_window = Tk()
  ex_window.title("Export")
  ex_window.geometry("200x200")
  ex_label=Label(ex_window, text = "Filename:", bg = label_colour)
  ex_label.pack()
  ex_entry = Entry(ex_window, font = (myfont, 12))
  ex_entry.pack()
  ex_button = Button(ex_window, text = "Export", command = createExcel, bg = button_colour)
  ex_button.pack()
  ex_window.mainloop()
