# -*- coding: utf8 -*-
from Tkinter import *
root = Tk()
menubar = Menu(root)

def printItem():
    print 'add_separator'

filemenu = Menu(menubar,tearoff = 0)
for k in range(5):
    filemenu.add_command(label = str(k),command = printItem)
menubar.add_cascade(label = 'Language',menu = filemenu)

'''以下为向菜单中添加项的操作'''
#在索引1添加一菜单command项
filemenu.insert_command(1,label = '1000',command = printItem)
#在索引2添加一菜单checkbutton项
filemenu.insert_checkbutton(2,label = '2000',command = printItem)
#在索引3添加一菜单radiobutton项
filemenu.insert_radiobutton(3,label = '3000',command = printItem)
#将新添加的菜单项使用分隔符隔开
filemenu.insert_separator(1)
filemenu.insert_separator(5)

'''以下为删除菜单项的操作'''
#删除索引6-9的菜单项
filemenu.delete(6,9)
#删除索引为0的菜单项
filemenu.delete(0)

root['menu'] = menubar
root.mainloop()
#分隔符将相关的菜单项进行分组，只是UI上的实现，程序上没有任何改变，它也不执行任何的命令
