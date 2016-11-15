from Tkinter import *
root = Tk()
lb = Listbox(root)
for i in range(10):
    lb.insert(END,str(i))
lb.delete(1,3)   #delete  item 1 ` item 3
lb.pack()
root.mainloop()
