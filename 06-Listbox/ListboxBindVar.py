# -*- coding: cp936 -*-
from Tkinter import *
root = Tk()
v = StringVar()
lb = Listbox(root,listvariable = v)
for i in range(10):
    lb.insert(END,str(i*100))
print v.get()
v.set(('1000','200'))
lb.pack()
root.mainloop()
