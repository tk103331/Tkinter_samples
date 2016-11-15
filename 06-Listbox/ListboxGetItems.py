from Tkinter import *
root = Tk()
lb = Listbox(root)
for i in range(10):
    lb.insert(END,str(i*100))
print lb.get(3,7)   
lb.pack()
root.mainloop()
