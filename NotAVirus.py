from tkinter import *
from tkinter import ttk
a = 1


def init():
    b = 1
    while b < 6:
        root = Tk()
        frm = ttk.Frame(root, padding=300)
        frm.grid()
        ttk.Label(frm, text="Click to close.").grid(column=0, row=0)
        ttk.Button(frm, text="Quit", command=init).grid(column=1, row=0)
        b = b + 1

while a < 200:
    root = Tk()
    frm = ttk.Frame(root, padding=300)
    frm.grid()
    ttk.Label(frm, text="Click to close.").grid(column=0, row=0)
    ttk.Button(frm, text="Quit", command=init).grid(column=1, row=0)
    
    a = a +1



