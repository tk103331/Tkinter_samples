from Tkinter import *
root = Tk()
v = IntVar()
v.set(1)
for i in range(3):
    Radiobutton(root,
                variable = v,
                value = 1,
                text = 'python' + str(i)
                ).pack()
for i in range(3):
    Radiobutton(root,
                    variable = v,
                    value = i,
                    text = 'python' + str(2 + i)
                    ).pack()
root.mainloop()
