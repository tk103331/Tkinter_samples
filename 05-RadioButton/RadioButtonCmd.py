from Tkinter import *
root = Tk()
v = IntVar()
v.set(0)
def r1():
    print 'call r1'
def r2():
    print 'call r2'
def r3():
    print 'call r3'
def r4():
    print 'call r4'
i = 0

for r in [r1,r2,r3,r4]:
    Radiobutton(root,
                    variable = v,
                    text = 'radio button',
                    value = i,
                    command = r
                    ).pack()
    i += 1
    
root.mainloop()
