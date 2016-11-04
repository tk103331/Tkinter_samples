from Tkinter import *
root = Tk()

v = StringVar()
def callCheckbutton():
    print v.get()
Checkbutton(root,
            variable = v,
            text = 'checkbutton value',
            onvalue = 'python', 
            offvalue = 'tkinter',
            command = callCheckbutton).pack()
root.mainloop()

            
