from Tkinter import *
root = Tk()
def func():
    print v.get()
v = IntVar()
v.set(1)
for i in range(3):
    Radiobutton(root,variable = v,text = 'python',value = i,command=func).pack()

root.mainloop()
