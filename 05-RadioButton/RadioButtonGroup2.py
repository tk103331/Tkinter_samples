from Tkinter import *
root = Tk()
vLang = IntVar()
vOS = IntVar()
vLang.set(1)
vOS.set(2)

for v in [vLang,vOS]: 
    for i in range(3): 
        Radiobutton(root,
                    variable = v,
                    value = i,
                    text = 'python' + str(i)
                    ).pack()
root.mainloop()
