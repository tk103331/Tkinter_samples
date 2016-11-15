# -*- coding: cp936 -*-
from Tkinter import *
root = Tk()
def printList(event):
    print lb.get(lb.curselection()) 
lb = Listbox(root)
lb.bind('<Double-Button-1>',printList)
for i in range(10):
    lb.insert(END,str(i*100))
lb.pack()
root.mainloop()
