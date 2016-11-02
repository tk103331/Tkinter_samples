from Tkinter import *

def helloButton():
    print 'hello button'
root = Tk()

Button(root,text = 'Hello Button',command = helloButton).pack()
root.mainloop()
