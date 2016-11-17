# -*- coding: utf8 -*-
from Tkinter import *
root = Tk()
#每次打印出各个变量的当前值
def printItem():
    print 'Python = ',vPython.get()
    print 'PHP = ',vPHP.get()
    print 'CPP = ',vCPP.get()
    print 'C = ',vC.get()
    print 'Java = ',vJava.get()
    print 'JavaScript = ',vJavaScript.get()
    print 'VBScript = ',vVBScript.get()
    
menubar = Menu(root)

vPython = StringVar()
vPHP     = StringVar()
vCPP     = StringVar()
vC         = StringVar()
vJava     = StringVar()
vJavaScript = StringVar()
vVBScript     = StringVar()

filemenu = Menu(menubar,tearoff = 0)
for k,v in {'Python':vPython,
               'PHP':vPHP,
               'CPP':vCPP,
               'C':vC,
               'Java':vJava,
               'JavaScript':vJavaScript,
               'VBScript':vVBScript}.items():
    #绑定变量与回调函数
    filemenu.add_checkbutton(label = k,command = printItem,variable = v)
#将menubar的menu属性指定为filemenu，即filemenu为menubar的下拉菜单
menubar.add_cascade(label = 'Language',menu = filemenu)
root['menu'] = menubar
root.mainloop()
#程序运行，使用了Checkbutton，并通过printItem将每个Checkbutton在当前值打印出来。
