import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as ttk

app = ttk.Tk()
app.title('Treadmil Users Analysis')
app.geometry('600x300') 

rb1 = ttk.Variable(app)
values = {'Data 1': '1','Data 2': '2'}
for key,value in values.items():
    ttk.Radiobutton(app,text = key,variable = rb1 , value = value).pack()

def show():
    print(rb1.get())

ttk.Button(app,text = 'Show',command = show).place(x=400,y=10)

app.mainloop()