from Tkinter import *

def cb1():
    print 'button1 clicked'
def cb2(event):
    print 'button2 clicked'
def cb3():
    print 'button3 clicked'
    
root = Tk()

b1 = Button(root,text = 'Button1',command = cb1)
b2 = Button(root,text = 'Button2')
b2.bind("<Return>",cb2)
b3 = Button(root,text = 'Button3',command = cb3)
b1.pack()
b2.pack()
b3.pack()

b2.focus_set()
root.mainloop()
