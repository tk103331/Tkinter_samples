from Tkinter import *
root = Tk()
lb = Listbox(root)
for i in range(10):
    lb.insert(END,str(i))
lb.selection_set(0,10)   #select item 0 to item 10
lb.selection_clear(0,3)  #clear select item 0 to item 3
lb.pack()
root.mainloop()
