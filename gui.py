from tkinter import *
from socketpy import sio


def printtext():
    global uuid, alias
    uuidStr = uuid.get()
    aliasStr = alias.get()
    print(uuidStr, aliasStr)
    if (uuidStr == None or aliasStr == None):
        return
    else:
        sio.emit('add user', {"uuid": uuidStr, "alias": aliasStr})
        root.destroy()

root = Tk()
root.title("Piston Print")
root.geometry("270x150+30+30")

uuid_label = Label(root, text="Please Enter Token ")
uuid = Entry(root)

alias_label = Label(root, text="Please Enter Alias ")
alias = Entry(root)

b = Button(root, text="Submit", command=printtext)

uuid_label.grid(row=0, sticky="nsew")
uuid.grid(row=0, column=1, sticky="nsew")
alias_label.grid(row=1, sticky="nsew")
alias.grid(row=1, column=1, sticky="nsew")
b.grid(row=2, columnspan=2, padx=50, sticky="nsew")
root.mainloop()
