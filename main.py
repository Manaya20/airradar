import tkinter
import pandas as pd
from tkinter import *
from tkinter.ttk import *
import numpy as np
import sys
df=pd.read_csv('/Users/manayapachpor/Downloads/airradar/BLR_DEPARTURE.csv', encoding='unicode_escape')
MainWindow = Tk()
MainWindow.geometry("800x400")
MainWindow.title('AIRADAR')
MainWindow.configure(bg='black')

def display_src():
    newWindow = Toplevel(MainWindow)
    newWindow.title("Display Source")
    newWindow.geometry("2000x2000")
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
    disp.place(x=20, y=30)
    disp = Entry(newWindow, textvariable=var)
    disp.place(x=220, y=30)
    b_get_1=Button(newWindow, text="RUN",command=get_1)
    b_get_1.place(x=200, y=100)

def terminal():
    newWindow = Toplevel(MainWindow)
    newWindow.title("Display Flight with Specified Terminal")
    newWindow.geometry("2000x2000")
    newWindow.configure(bg='black')
    var = tkinter.StringVar()
    def get_1():
        model=var.get()
        disp_1 = df.loc[(df['Arrival_terminal']==model),['Flight_No','Airlines_Name','Arrival_Airport']]
        txt = Text(newWindow)
        txt.pack()
        class PrintToTXT(object):
            def write(self, s):
                txt.insert(END, s)
        sys.stdout = PrintToTXT()
        print(disp_1)
    disp = tkinter.Label(newWindow,bg='black',fg='white', text="Enter Terminal Number ", font=('bold', 20))
    disp.place(x=20, y=30)
    disp = tkinter.Entry(newWindow, bg='black',fg='white',textvariable=var)
    disp.place(x=300, y=30)
    b_get_1=Button(newWindow, text="RUN",command=get_1)
    b_get_1.place(x=200, y=100)


def exitWindow():
    sys.exit()

dispBtn=tkinter.Button(MainWindow,text="DISPLAY FLIGHT SOURCE",command=display_src,bg='black')
dispBtn.configure(bg='black')
dispBtn.place(x=23, y=50)

terBtn=tkinter.Button(MainWindow, bg='black',text="DISPLAY TERMINAL", command=terminal)
terBtn.place(x=320, y=50)

extBtn=tkinter.Button(MainWindow, bg='black',text="Exit", command=exitWindow)
extBtn.place(x=480, y=210)

MainWindow.mainloop()
