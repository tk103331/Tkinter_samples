from Tkinter import *
root = Tk()
e = StringVar()
entry = Entry(root,textvariable = e)
e.set('input your text here')
entry.pack()
root.mainloop()

