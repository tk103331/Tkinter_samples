# -*- coding: utf8 -*-
#添加菜单hello和quit，将hello菜单与hello函数绑定；quit菜单与root.quit绑定

from Tkinter import *
root = Tk()
def hello():
    print 'hello menu'
menubar = Menu(root)
#创建主菜单，每个菜单对应的回调函数都是hello
for item in ['Python','PHP','CPP','C','Java','JavaScript','VBScript']:
    menubar.add_command(label = item,command = hello)
#将root的menu属性设置为menubar
root['menu'] = menubar
root.mainloop()
#这个菜单没有下拉菜单，仅包含两个菜单项
