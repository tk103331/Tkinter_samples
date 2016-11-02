from Tkinter import *
def printEventInfo(event):
    print 'event.time = ' , event.time
    print 'event.type = ' , event.type
    print 'event.WidgetId = ', event.widget
    print 'event.KeySymbol = ',event.keysym
root = Tk()
b = Button(root,text = 'Infomation')
b.bind("<Return>",printEventInfo)
b.pack()
b.focus_set()
root.mainloop() 
