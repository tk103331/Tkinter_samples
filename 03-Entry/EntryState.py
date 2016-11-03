from Tkinter import *
root = Tk()
e = StringVar()
entry = Entry(root,textvariable = e)
e.set('input your text here')
entry.pack()
entry['state'] = 'readonly'  #normal/active/disabled
root.mainloop()
