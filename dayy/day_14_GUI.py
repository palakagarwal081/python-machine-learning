# GUI - Graphicla User Interface

# Libraries
###################
# 1. Tkinter
# 2. PyQT
# 3. Turtle

import tkinter as ttk
app = ttk.Tk()
app.title('My App')
app.geometry('800x600')

msg = ttk.Variable(app)
# print(msg.get())
# msg.set('Empty')
# print(msg.get())

ttk.Label(app, text = 'A simple Text Label').place(x=40,y=40)
ttk.Label(app, text = 'Heyy Palak here').place(x=60,y=60)
ttk.Label(app,textvariable=msg,font = ('Arial',11)).place(x=100,y=80)

def abc():
    print('Wow')
    msg.set('Jo tera mann kare')

ttk.Button(app,text = 'Isko Click Kardo',font = ('Arial',11),command = abc).place(x=100,y=100)
ttk.Button(app,text = 'Ye wala bhi hai',font = ('Arial',11),command = lambda:msg.set('pata nhi')).place(x=100,y=130)
# command mein ek function de dete h

f1 = ttk.Variable(app)
f1.set('0')
f2 = ttk.Variable(app)
f2.set('0')
result = ttk.Variable(app)

ttk.Entry(app,textvariable=f1,width = 4,font = ('Arial',11)).place(x=50,y=200)
ttk.Entry(app,textvariable=f2,width = 4,font = ('Arial',11)).place(x=100,y=200)
ttk.Label(app,text='Result').place(x=220,y=220)
ttk.Label(app,textvariable=result, font = ('Arial',11)).place(x=240,y=160)

def calci(op):
    print('I will calculate')
    result.set(eval(f1.get()+op+f2.get())) #eval is a function which evaluate the python string and solve it and treat python string as python function

ttk.Button(app,text='+',command=lambda:calci('+'), font = ('Arial',11)).place(x=50,y=240)
ttk.Button(app,text='-',command=lambda:calci('-'), font = ('Arial',11)).place(x=70,y=240)
ttk.Button(app,text='*',command=lambda:calci('*'), font = ('Arial',11)).place(x=90,y=240)
ttk.Button(app,text='/',command=lambda:calci('/'), font = ('Arial',11)).place(x=110,y=240)

box = ttk.Listbox(app, height=5, fg='red',activestyle='dotbox')  # fg for foreground colour
box.insert(1,'Sample1')
box.insert(2,'Sample2')
box.insert(3,'Sample3')
box.place(x=350,y=40)

def show():
    print(box.get(box.curselection()))
    
ttk.Button(app,text='Show',command=show).place(x=350,y=250)




app.mainloop()