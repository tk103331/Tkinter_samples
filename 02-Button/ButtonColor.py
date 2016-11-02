from Tkinter import *
root = Tk()
bfg = Button(root,text = 'change foreground',fg = 'red')
bfg.pack()

bbg = Button(root,text = 'change backgroud',bg = 'blue')
bbg.pack()

root.mainloop()
