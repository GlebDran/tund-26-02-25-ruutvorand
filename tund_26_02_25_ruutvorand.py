from tkinter import *

def aken():
    aken=Tk()
    aken.geometry("650x260")
    aken.title("Ruutvõrrand")
    f1=Frame(aken, width=650, height=260)
    f1.pack()
    lbl=Label(f1, text="Ruutvõrrandite lahendamine",font="Calibri 26", fg="green", bg="lightblue")
    lbl.pack(side=TOP)
    lbl_vastus=Label(1, text="lahendamine", height=4, width=60)

aken()