from Tkinter import *
root = Tk()
lb = Listbox(root)
for item in ['python','tkinter','widget']:
    lb.insert(END,item)
lb.pack()
root.mainloop()
