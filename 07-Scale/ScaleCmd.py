# -*- coding: cp936 -*-
from Tkinter import *

root = Tk()
def printScale(text):
    print 'text = ',text
    print 'v = ',v.get()
v = StringVar()
Scale(root,
      from_ = 0,
      to = 100.0,
      resolution = 0.0001,
      orient = HORIZONTAL,
      variable = v,
      command = printScale
      ).pack()
print v.get()
root.mainloop()
