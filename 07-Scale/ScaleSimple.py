# -*- coding: cp936 -*-
from Tkinter import *
root = Tk()
Scale(root,
      from_ = -500,
      to = 500,
      resolution = 5,
      orient = HORIZONTAL
      ).pack()
root.mainloop()
