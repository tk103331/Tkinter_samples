from Tkinter import *
root = Tk()
e = StringVar()
entry = Entry(root,textvariable = e)
e.set('input your text here')
entry.pack()

entry['show'] = '*'

for mask in ['*','#','%']:
    e = StringVar()
    entry = Entry(root,textvariable = e)
    e.set('password')
    entry.pack()
    entry['show'] = mask

root.mainloop()

