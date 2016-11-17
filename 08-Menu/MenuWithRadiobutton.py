# -*- coding: utf8 -*-
from Tkinter import *
root = Tk()

menubar = Menu(root)
vLang = StringVar()
#每次打印出当前选中的语言
def printItem():
    print 'vLang = ',vLang.get()
filemenu = Menu(menubar,tearoff = 0)
for k in ['Python','PHP','CPP','C','Java','JavaScript','VBScript']:
    #绑定变量与回调函数，指定的变量vLang将这几项划为一组
    filemenu.add_radiobutton(label = k,command = printItem,variable = vLang)
#将menubar的menu属性指定为filemenu，即filemenu为menubar的下拉菜单
menubar.add_cascade(label = 'Language',menu = filemenu)
root['menu'] = menubar
root.mainloop()
#程序每次打印出当前选中的语言
#与Checkbutton不同的是，同一个组内只有一个处于选中状态。
