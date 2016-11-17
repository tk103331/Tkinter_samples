# -*- coding: utf8 -*-
from Tkinter import *
root = Tk()
def hello():
    print 'hello menu'
menubar = Menu(root)

filemenu = Menu(menubar,tearoff = 0)
for item in ['Python','PHP','CPP','C','Java','JavaScript','VBScript']:
    filemenu.add_command(label = item,command = hello)
#将menubar的menu属性指定为filemenu，即filemenu为menubar的下拉菜单
menubar.add_cascade(label = 'Language',menu = filemenu)
root['menu'] = menubar
root.mainloop()
