from Tkinter import *
root = Tk()

Label(root,text = 'bottom',compound = 'bottom',bitmap = 'error').pack()

Label(root,text = 'top',compound = 'top',bitmap = 'error').pack()

Label(root,text = 'right',compound = 'right',bitmap = 'error').pack()

Label(root,text = 'left',compound = 'left',bitmap = 'error').pack()

Label(root,text = 'center',compound = 'center',bitmap = 'error').pack()

root.mainloop()
