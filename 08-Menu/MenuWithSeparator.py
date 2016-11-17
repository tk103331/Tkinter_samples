# -*- coding: utf8 -*-
from Tkinter import *
root = Tk()
menubar = Menu(root)
vLang = StringVar()
#每次打印出当前选中的语言
def printItem():
    print 'add_separator'

filemenu = Menu(menubar,tearoff = 0)
for k in ['Python','PHP','CPP','C','Java','JavaScript','VBScript']:
    filemenu.add_command(label = k,command = printItem)
    #将各个菜单项使用分隔符隔开
    filemenu.add_separator()
menubar.add_cascade(label = 'Language',menu = filemenu)
root['menu'] = menubar
root.mainloop()
#分隔符将相关的菜单项进行分组，只是UI上的实现，程序上没有任何改变，它也不执行任何的命令
