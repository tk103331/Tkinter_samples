from Tkinter import *
def callCheckbutton():
    print 'you check this button'
root = Tk()
Checkbutton(root,text = 'check python',command = callCheckbutton).pack()
root.mainloop()
