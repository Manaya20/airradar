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

def distance():
    newWindow = Toplevel(MainWindow)
    newWindow.title("Flight details with Specified Distance")
    newWindow.geometry("2000x2000")
    newWindow.configure(bg='black')
    var = tkinter.StringVar()
    var2 = tkinter.StringVar()
    def get_1():
        model = var.get()
        dist=var2.get()
        disp_1 = df.loc[((df['Flight_No']==model) & (df['Flight_distance']==dist)), ['Flight_No','Airlines_Name','Flight_distance']]
        txt = Text(newWindow)
        txt.pack()
        class PrintToTXT(object):
            def write(self, s):
                txt.insert(END, s)
        sys.stdout = PrintToTXT()
        print(disp_1)
    disp = tkinter.Label(newWindow, bg='black',fg='white',text="Enter Flight Number ", font=('bold', 20))
    disp.place(x=20, y=30)
    disp = tkinter.Entry(newWindow, bg='black',fg='white',textvariable=var)
    disp.place(x=300, y=30)
    disp2 = tkinter.Label(newWindow,bg='black',fg='white', text="Enter Distance ", font=('bold', 20))
    disp2.place(x=20, y=60)
    disp2 = tkinter.Entry(newWindow,bg='black',fg='white', textvariable=var2)
    disp2.place(x=300, y=60)
    b_get_1 = Button(newWindow, text="RUN", command=get_1)
    b_get_1.place(x=200, y=100)

def status():
    newWindow = Toplevel(MainWindow)
    newWindow.title("Flight details with Specified Distance")
    newWindow.geometry("2000x2000")
    newWindow.configure(bg='black')
    var = tkinter.StringVar()
    var2 = tkinter.StringVar()
    var3=tkinter.StringVar()
    def get_1():
        model = var.get()
        city_code = var2.get()
        date=var3.get()
        disp_1 = df.loc[(df['Flight_No']==model)&(df['Arrival_City_Code']==city_code)&(df['Date_wise']==date),['Date_wise','Flight_No','Airlines_Name','Flight_Time_status']]
        txt = Text(newWindow)
        txt.pack()
        class PrintToTXT(object):
            def write(self, s):
                txt.insert(END, s)
        sys.stdout = PrintToTXT()
        print(disp_1)
    disp = tkinter.Label(newWindow, bg='black',fg='white',text="Enter Flight Number ", font=('bold', 20))
    disp.place(x=20, y=30)
    disp = tkinter.Entry(newWindow, bg='black',fg='white',textvariable=var)
    disp.place(x=300, y=30)
    disp2 = tkinter.Label(newWindow, bg='black',fg='white',text="Arrival City Code ", font=('bold', 20))
    disp2.place(x=20, y=60)
    disp2 = tkinter.Entry(newWindow, bg='black',fg='white',textvariable=var2)
    disp2.place(x=300, y=60)
    disp3 = tkinter.Label(newWindow, bg='black',fg='white',text="Date ", font=('bold', 20))
    disp3.place(x=20, y=90)
    disp3 = tkinter.Entry(newWindow, bg='black',fg='white',textvariable=var3)
    disp3.place(x=300, y=90)
    b_get_1 = tkinter.Button(newWindow, text="RUN", command=get_1)
    b_get_1.place(x=200, y=200)

def aircraft():
    newWindow = Toplevel(MainWindow)
    newWindow.title("Aircraft Details")
    newWindow.geometry("2000x2000")
    newWindow.configure(bg='black')
    var = tkinter.StringVar()
    var2 = tkinter.StringVar()
    def get_1():
        model = var.get()
        city_code = var2.get()
        disp_1 = df.loc[((df['Flight_No'] == model) & (df['Arrival_City_Code'] == city_code)), ['Flight_No','Airlines_Name','Aircraft_equipment_description']]
        txt = Text(newWindow)
        txt.pack()
        class PrintToTXT(object):
            def write(self, s):
                txt.insert(END, s)
        sys.stdout = PrintToTXT()
        print(disp_1)
    disp = tkinter.Label(newWindow, bg='black',fg='white',text="Enter Flight Number ", font=('bold', 20))
    disp.place(x=20, y=30)
    disp = tkinter.Entry(newWindow, bg='black',fg='white',textvariable=var)
    disp.place(x=300, y=30)
    disp2 = tkinter.Label(newWindow, bg='black',fg='white',text="Enter Arrival City Code ", font=('bold', 20))
    disp2.place(x=20, y=60)
    disp2 = tkinter.Entry(newWindow, bg='black',fg='white',textvariable=var2)
    disp2.place(x=300, y=60)
    b_get_1 = Button(newWindow, text="RUN", command=get_1)
    b_get_1.place(x=200, y=100)

def delay():
    newWindow = Toplevel(MainWindow)
    newWindow.title("Flight Delay Details")
    newWindow.geometry("2000x2000")
    newWindow.configure(bg='black')
    var = tkinter.StringVar()
    var2 = tkinter.StringVar()
    var3 = tkinter.StringVar()
    def get_1():
        model = var.get()
        status = var2.get()
        date = var3.get()
        disp_1 = df.loc[(df['Flight_No'] == model) & (df['Flight_Time_status'] == status)& (df['Date_wise'] == date), ['Flight_No', 'Airlines_Name','Flight_delay_by_time','Arrivial_time_estimated']]
        txt = Text(newWindow)
        txt.pack()

        class PrintToTXT(object):
            def write(self, s):
                txt.insert(END, s)

        sys.stdout = PrintToTXT()
        print(disp_1)

    disp = tkinter.Label(newWindow, bg='black',fg='white',text="Enter Flight Number ", font=('bold', 20))
    disp.place(x=20, y=30)
    disp = tkinter.Entry(newWindow, bg='black',fg='white',textvariable=var)
    disp.place(x=300, y=30)
    disp2 = tkinter.Label(newWindow, text="Status ", bg='black',fg='white',font=('bold', 20))
    disp2.place(x=20, y=60)
    disp2 = tkinter.Entry(newWindow, bg='black',fg='white',textvariable=var2)
    disp2.place(x=300, y=60)
    disp3 = tkinter.Label(newWindow, text="Date ", bg='black',fg='white',font=('bold', 20))
    disp3.place(x=20, y=90)
    disp3 = tkinter.Entry(newWindow, bg='black',fg='white',textvariable=var3)
    disp3.place(x=300, y=90)
    b_get_1 = Button(newWindow, text="RUN", command=get_1)
    b_get_1.place(x=200, y=200)
    
def detail():
    newWindow = Toplevel(MainWindow)
    newWindow.title("Flight Details")
    newWindow.geometry("2000x2000")
    newWindow.configure(bg='black')
    var = tkinter.StringVar()
    var2 = tkinter.StringVar()
    def get_1():
        city = var.get()
        date = var2.get()
        disp_1 = df.loc[((df['Arrival_City'] == city)&(df['Date_wise']==date)),['Date_wise','Flight_No', 'Airlines_Name','Departure_Date','Departure_time_estimated','Arrival_Date','Arrivial_time_estimated']]
        txt = Text(newWindow)
        txt.pack()

        class PrintToTXT(object):
            def write(self, s):
                txt.insert(END, s)

        sys.stdout = PrintToTXT()
        print(disp_1)

    disp = tkinter.Label(newWindow, bg='black',fg='white',text="Enter City ", font=('bold', 20))
    disp.place(x=20, y=30)
    disp = tkinter.Entry(newWindow, bg='black',fg='white',textvariable=var)
    disp.place(x=300, y=30)
    disp2 = tkinter.Label(newWindow, bg='black',fg='white',text="Enter Date ", font=('bold', 20))
    disp2.place(x=20, y=60)
    disp2 = tkinter.Entry(newWindow, bg='black',fg='white',textvariable=var2)
    disp2.place(x=300, y=60)
    b_get_1 = Button(newWindow, text="RUN", command=get_1)
    b_get_1.place(x=200, y=100)


def exitWindow():
    sys.exit()

dispBtn=tkinter.Button(MainWindow,text="DISPLAY FLIGHT SOURCE",command=display_src,bg='black')
dispBtn.configure(bg='black')
dispBtn.place(x=23, y=50)

terBtn=tkinter.Button(MainWindow, bg='black',text="DISPLAY TERMINAL", command=terminal)
terBtn.place(x=320, y=50)

distBtn=tkinter.Button(MainWindow, bg='black',text="DISPLAY DISTANCE", command=distance)
distBtn.place(x=600, y=50)

statBtn=tkinter.Button(MainWindow, bg='black',text="DISPLAY FLIGHT STATUS",  command=status)
statBtn.place(x=70, y=130)

airBtn=tkinter.Button(MainWindow,  bg='black',text="DISPLAY AIRCRAFT DETAILS",  command=aircraft)
airBtn.place(x=290, y=130)

delayBtn=tkinter.Button(MainWindow,  bg='black',text="DISPLAY DELAY DETAILS",  command=delay)
delayBtn.place(x=560, y=130)

detailBtn=tkinter.Button(MainWindow,bg='black', text="DISPLAY FLIGHT DETAILS",  command=detail)
detailBtn.place(x=200, y=210)


extBtn=tkinter.Button(MainWindow, bg='black',text="Exit", command=exitWindow)
extBtn.place(x=480, y=210)

MainWindow.mainloop()


