from ast import For, If, In
from cProfile import label
import sqlite3, hashlib
from tkinter import *

from matplotlib import widgets
from matplotlib.pyplot import text

window = Tk()

window.title('Password Vault')

def firstScreen():

    window.geometry("250x150")

    lbl = Label(window, text="create Master Password")
    lbl.config(anchor=CENTER)
    lbl.pack()

    txt = Entry(window,width=20)
    txt.pack()
    txt.focus()

    lbl1 = Label(window, text="re-enter Password")
    lbl1.pack()

    txt1 = Entry(window,width=20)
    txt1.pack()
    txt1.focus()

    lbl2 = Label(window)
    lbl2.pack()

    def savePassword():
        if txt.get() == txt1.get():
            pass
        else:
            lbl2.config(text="passwords do not match")

    btn =Button(window, text="Submit", command=savePassword)
    btn.pack(pady=10)


def loginScreen():
    window.geometry("250x150")

    lbl = Label(window, text="Enter Master Password")
    lbl.config(anchor=CENTER)
    lbl.pack()

    txt = Entry(window,width=20)
    txt.pack()
    txt.focus()

    lbl1 = Label(window)
    lbl1.pack()

    def checkPassword():
        password = "test"

        if password == txt.get():
            passwordVault()

        else:
            txt.delete(0,'end')
            lbl1.config(text="wrong password")
        

    btn =Button(window, text="Submit", command=checkPassword)
    btn.pack(pady=10)


def passwordVault():
    for Widget in window.winfo_children():
        Widget.destroy()
        window.geometry("700x350")

        lbl = Label(window, text="Password Vault")
        lbl.config(anchor=CENTER)
        lbl.pack





firstScreen()


window.mainloop()

