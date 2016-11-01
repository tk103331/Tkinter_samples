from Tkinter import *
root = Tk()

Label(root,text = 'red',bg = 'red').pack()
Label(root,text = 'blue',bg = 'blue').pack()
Label(root,text = 'yellow',bg = 'yellow').pack()

Label(root,bg = 'red',width = 10,height = 3).pack()
Label(root,bg = 'blue',width = 10,height = 3).pack()
Label(root,bg = 'yellow',width = 10,height = 3).pack()
root.mainloop()
