from Tkinter import *
root = Tk()
lb = Listbox(root)
for item in ['python','tkinter','widget']:
    lb.insert(END,item)
lb.insert(ACTIVE,'current')
lb.insert(0,'linux','windows','unix')
lb.pack()
root.mainloop()
