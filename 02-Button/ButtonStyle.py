from Tkinter import *
root = Tk()
#flat, groove, raised, ridge, solid, or sunken
Button(root,text = 'hello button',relief=FLAT).pack()
Button(root,text = 'hello button',relief=GROOVE).pack()
Button(root,text = 'hello button',relief=RAISED).pack()
Button(root,text = 'hello button',relief=RIDGE).pack()
Button(root,text = 'hello button',relief=SOLID).pack()
Button(root,text = 'hello button',relief=SUNKEN).pack()

root.mainloop()
