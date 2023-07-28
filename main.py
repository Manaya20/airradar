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
MainWindow.configure(bg='black')

