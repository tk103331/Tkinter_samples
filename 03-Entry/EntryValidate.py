from Tkinter import *
root = Tk()
e = StringVar()
def validateText(contents):
    print contents
    return contents.isalnum()

entry = Entry(root,validate = 'key',textvariable = e,validatecommand = validateText)
entry.pack()

root.mainloop()
