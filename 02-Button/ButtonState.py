from Tkinter import *
root = Tk()
def statePrint():
    print 'state'
for r in ['normal','active','disabled']:
    Button(root,
    text = r,
    state = r,
    width = 30,
    command = statePrint).pack()
root.mainloop()
