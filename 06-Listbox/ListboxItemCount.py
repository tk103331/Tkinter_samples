from Tkinter import *
root = Tk()
lb = Listbox(root)
for i in range(10):
    lb.insert(END,str(i))
lb.delete(3)
print lb.size()
lb.pack()
root.mainloop()
