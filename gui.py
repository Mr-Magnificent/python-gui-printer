from tkinter import *
from socketpy import sio
from fileHandling import add
import os.path

uuid = alias = root = None


def printtext():
    global uuid, alias
    uuidStr = uuid.get() 
    aliasStr = alias.get()
    print(uuidStr, aliasStr)
    if (uuidStr == None or aliasStr == None):
        return
    else:
        seq = [uuidStr, aliasStr]
        sio.emit('add user', {"uuid": uuidStr, "alias": aliasStr})
        root.destroy()
        with open('credentials.txt', 'w') as file:
            file.writelines(seq)
        dirpath = os.path.dirname(os.path.abspath(__file__))
        add("Piston Print", dirpath + "socketpy.py")

def createGui():
    global uuid, alias, root
    root = Tk()
    root.title("Piston Print")
    root.geometry("270x150+30+30")

    uuid_label = Label(root, text="Please Enter Token* ")
    uuid = Entry(root)

    alias_label = Label(root, text="Please Enter Alias* ")
    alias = Entry(root)

    b = Button(root, text="Submit", command=printtext)

    uuid_label.grid(row=0, sticky="nsew")
    uuid.grid(row=0, column=1, sticky="nsew")
    alias_label.grid(row=1, sticky="nsew")
    alias.grid(row=1, column=1, sticky="nsew")
    b.grid(row=3, columnspan=2, padx=50, sticky="nsew")
    root.mainloop()


if not os.path.isfile('credentials.txt'):
    createGui()
