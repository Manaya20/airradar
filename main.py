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
    newWindow.configure(bg='black')
    var=tkinter.StringVar()
    def get_1():
        model=var.get()
        disp_1 = df.loc[(df['Flight_No']==model),['Flight_No','Airlines_Name','Arrival_City_Code']]
        txt = Text(newWindow)
        txt.pack()
        class PrintToTXT(object):
            def write(self, s):
                txt.insert(END, s)
        sys.stdout = PrintToTXT()
        print(disp_1)
    disp = tkinter.Label(newWindow,bg='black',fg='white', text="Enter Flight Number ", font=('bold', 20))
    disp.configure(bg='black',fg="white")
    disp.place(x=20, y=30)
    disp = Entry(newWindow, textvariable=var)
    b_get_1=tkinter.Button(newWindow, text="RUN",bg='black')
    b_get_1.configure(bg='black')
    b_get_1.place(x=160, y=100)

dispBtn=tkinter.Button(MainWindow,text="FLIGHT SOURCE",bg='black',command=display_src)
dispBtn.configure(bg='black')
dispBtn.place(x=23, y=50)





MainWindow.mainloop()
