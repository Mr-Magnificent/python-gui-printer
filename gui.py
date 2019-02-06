from tkinter import *

def printtext():
    global e
    string = e.get()
    e.delete(0, 'end')
    print (string)

root = Tk()
root.geometry()
root.title("Piston Print")

e = Entry(root)
e.pack(side=LEFT)
e.focus_set()

b = Button(root, text="Submit", command=printtext)
b.pack(side=BOTTOM)
root.mainloop()


