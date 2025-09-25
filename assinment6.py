#tkinter  calculator

import math
from re import I
from tkinter import *

win=Tk()
win.geometry("500x500")

e=Entry(win,width=56,border=5)
e.place(x=0,y=0)


def click(num):
    result= e.get()
    e.delete(0,END)
    e.insert(0,str(result)+str(num))


b=Button(win,text="1",width=12,command=lambda:click(1))
b.place(x=10,y=60)

b=Button(win,text="2",width=12,command=lambda:click(2))
b.place(x=80,y=60)

b=Button(win,text="3",width=12,command=lambda:click(3))
b.place(x=170,y=60)

b=Button(win,text="4",width=12,command=lambda:click(4))
b.place(x=10,y=120)

b=Button(win,text="5",width=12,command=lambda:click(5))
b.place(x=80,y=120)

b=Button(win,text="6",width=12,command=lambda:click(6))
b.place(x=170,y=120)

b=Button(win,text="7",width=12,command=lambda:click(7))
b.place(x=10,y=180)

b=Button(win,text="8",width=12,command=lambda:click(8))
b.place(x=80,y=180)

b=Button(win,text="9",width=12,command=lambda:click(9))
b.place(x=170,y=180)

b=Button(win,text="0",width=12,command=lambda:click(0))
b.place(x=10,y=240)

#-----------------------------


def add():
    n1=e.get()
    global math
    math="addition"
    global i 
    i=int(n1)
    e.delete(0,END)
b=Button(win,text="+",width=12,command=add)
b.place(x=80,y=240)

def sub():
    n1=e.get()
    global math
    math="subtraction"
    global i 
    i=int(n1)
    e.delete(0,END)

b=Button(win,text="-",width=12,command=sub)
b.place(x=170,y=240)

def multi():
    n1=e.get()
    global math
    math="multiplication"
    global i 
    i=int(n1)
    e.delete(0,END)

b=Button(win,text="*",width=12,command=multi)
b.place(x=10,y=300)

def div():
    n1=e.get()
    global math 
    math="devision"
    global i 
    i=int(n1)
    e.delete(0,END)

b=Button(win,text="/",width=12,command=div)
b.place(x=80,y=300)


def equal():
    n2=e.get()
    e.delete(0,END)
    if math=="addition":
        e.insert(0,i+int(n2))

    elif math=="subtraction":
        e.inster(0,i-int(n2))

    elif math=="multiplication":
        e.insert(0,i * int(n2))

    elif math== "devision":
        e.insert(0, i/int(n2))



b=Button(win,text="=",width=12,command=equal)
b.place(x=170,y=300)

def clear():
    e.delete(0,END)

b=Button(win,text="clear",width=12,command=clear)
b.place(x=10,y=350)

win.mainloop()