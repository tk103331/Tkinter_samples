from Tkinter import *
root = Tk()

v = IntVar()
def callCheckbutton():
    print v.get()
Checkbutton(root,
            variable = v,
            text = 'checkbutton value',
            command = callCheckbutton).pack()
root.mainloop()
