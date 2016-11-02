from Tkinter import *
root = Tk()
for a in ['n','s','e','w','ne','nw','se','sw']:
    Button(root,
    text = 'anchor',
    anchor = a,
    width = 30,
    height = 4).pack()

# Button(root,text = 'anchor',width = 30,height =4).pack()
# Button(root,text = 'anchor',anchor = 'center',width = 30,height =4).pack()
# Button(root,text = 'anchor',anchor = 'n',width = 30,height = 4).pack()
# Button(root,text = 'anchor',anchor = 's',width = 30,height = 4).pack()
# Button(root,text = 'anchor',anchor = 'e',width = 30,height = 4).pack()
# Button(root,text = 'anchor',anchor = 'w',width = 30,height = 4).pack()
# Button(root,text = 'anchor',anchor = 'ne',width = 30,height = 4).pack()
# Button(root,text = 'anchor',anchor = 'nw',width = 30,height = 4).pack()
# Button(root,text = 'anchor',anchor = 'se',width = 30,height = 4).pack()
# Button(root,text = 'anchor',anchor = 'sw',width = 30,height = 4).pack()

root.mainloop()
