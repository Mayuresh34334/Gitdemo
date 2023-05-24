from tkinter import *
import sqlite3
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import numpy as np
from tkcalendar import Calendar
import datetime

#connecting to database
try:
    conn = sqlite3.connect('ExpenseTracker.db') #database path
    cur = conn.cursor()
except:
    print("Unable to connect to database")


label_colour = "#e1ddd7"
button_colour = "#f9f6f6"   
myfont = ('Inter')

temp = Tk()
width= temp.winfo_screenwidth()               
height= temp.winfo_screenheight()
temp.destroy()