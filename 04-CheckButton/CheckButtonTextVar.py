from Tkinter import *
def callCheckbutton():
    v.set('check Tkinter')
    print v.get()

root = Tk()
v = StringVar()
v.set('check python')

Checkbutton(root,text = 'check python',textvariable = v,command = callCheckbutton).pack()

root.mainloop()
