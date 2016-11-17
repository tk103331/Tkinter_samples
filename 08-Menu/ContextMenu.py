# -*- coding: utf8 -*-
#方法是通过绑定鼠标右键，每当点击时弹出这个菜单，去掉与root的关联

from Tkinter import *
root = Tk()
menubar = Menu(root)

def printItem():
    print 'popup menu'

filemenu = Menu(menubar,tearoff = 0)
for k in ['Python','PHP','CPP','C','Java','JavaScript','VBScript']:
    filemenu.add_command(label = k,command = printItem)
    filemenu.add_separator()
menubar.add_cascade(label = 'Language',menu = filemenu)
#此时就不要将root的menu设置为menubar了
#root['menu'] = menubar
def popup(event):
    #显示菜单
    menubar.post(event.x_root,event.y_root)
#在这里相应鼠标的右键事件，右击时调用popup,此时与菜单绑定的是root，可以设置为其它的控件，在绑定的控件上右击就可以弹出菜单
root.bind('<Button-3>',popup)
root.mainloop()
#运行测试一个，可以看到各个菜单 项的功能都是可以使用的，所以弹出菜单与一般的菜单功能是一样的，只是弹出的方式不同而已。
