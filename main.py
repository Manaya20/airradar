import tkinter
import pandas as pd
from tkinter import *
from tkinter.ttk import *
import numpy as np
import sys
df=pd.read_csv('/Users/manayapachpor/Downloads/BLR_DEPARTURE.csv', encoding='unicode_escape')
MainWindow = Tk()
MainWindow.geometry("800x400")
MainWindow.title('AIRADAR')
MainWindow.configure(bg='White')

def display_src():
    newWindow = Toplevel(MainWindow)
    newWindow.title("SOURCE")
    newWindow.geometry("900x600")
    #newWindow.configure(bg='black')
   
    disp = tkinter.Label(newWindow, text="Enter Flight Number ")
    disp.place(x=20, y=30)
    
    b_get_1=tkinter.Button(newWindow, text="RUN",bg='black')
    b_get_1.configure(bg='black')
    b_get_1.place(x=160, y=100)

dispBtn=tkinter.Button(MainWindow,text="FLIGHT SOURCE",bg='black',command=display_src)
dispBtn.configure(bg='black')
dispBtn.place(x=23, y=50)
lb=tkinter.Label(MainWindow, text="Enter flight number",fg='white')
lb.place(x=23,y=39)
lb.pack()


MainWindow.mainloop()
