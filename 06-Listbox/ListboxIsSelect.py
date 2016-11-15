from Tkinter import *
root = Tk()
lb = Listbox(root)
for i in range(10):
    lb.insert(END,str(i*100))
lb.selection_set(3,8)
print lb.selection_includes(8)
print lb.selection_includes(0)

lb.pack()
root.mainloop()
