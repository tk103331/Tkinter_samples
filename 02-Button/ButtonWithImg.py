from Tkinter import *
root = Tk()

Button(root,text = 'botton',compound = 'bottom',bitmap = 'error').pack()
Button(root,text = 'top',compound = 'top',bitmap = 'error').pack()
Button(root,text = 'right',compound = 'right',bitmap = 'error').pack()
Button(root,text = 'left',compound = 'left',bitmap = 'error').pack()
Button(root,text = 'center',compound = 'center',bitmap = 'error').pack()

root.mainloop()
