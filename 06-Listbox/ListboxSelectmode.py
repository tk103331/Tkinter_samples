from Tkinter import *
root = Tk()
lb = Listbox(root,selectmode = EXTENDED)
#selectmode :  SINGLE  BROWSE  MULTIPLE  EXTENDED
for item in ['python','tkinter','widget']:
    lb.insert(END,item)
lb.pack()
root.mainloop()
