# -*- coding: cp936 -*-
from Tkinter import *
root = Tk()
v = StringVar()
Scale(root,
      from_ = 0,  
      to = 100.0,  
      resolution = 0.0001, 
      orient = HORIZONTAL, 
      variable = v
      ).pack()
print v.get()
root.mainloop()

