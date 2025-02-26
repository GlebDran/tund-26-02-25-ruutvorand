from tkinter import *
import math
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
from tkinter import messagebox


def Lahenda():
    pass

def Graafik():
    pass

def entryColor(event):
    i = entryA.get()
    if i.strip() == "":  # Убираем пробелы
        entryA.configure(bg="red")
    else:
        entryA.configure(bg="#ffe6f0")

    i = entryB.get()
    if i.strip() == "":
        entryB.configure(bg="red")
    else:
        entryB.configure(bg="#ffe6f0")

    i = entryC.get()
    if i.strip() == "":
        entryC.configure(bg="red")
    else:
        entryC.configure(bg="#ffe6f0")


def aken():
    global entryA, entryB, entryC  # Добавляем глобальные переменные #

    aken = Tk()
    aken.geometry("650x260")
    aken.resizable(False, False)
    aken.title("Ruutvõrrand")

    # Загрузка изображения
    try:
        original_image = Image.open(r"image.jpg")
        resized_image = original_image.resize((650, 260))
        bgimage = ImageTk.PhotoImage(resized_image)
        labelBG = Label(aken, image=bgimage)
        labelBG.place(x=0, y=0)
    except Exception as e:
        print("Ошибка загрузки изображения:", e)

    # Фрейм для элементов
    f1 = Frame(aken, width=650, height=260, bg="lightblue")
    f1.place(relx=0.5, rely=0.5, anchor=CENTER)

    lbl = Label(f1, text="Ruutvõrrandite lahendamine", font="Calibri 26", fg="green", bg="lightblue")
    lbl.pack(side=TOP)

    lbl_vastus = Label(f1, text="lahendamine", height=2, width=60, bg="yellow")
    lbl_vastus.pack(side=BOTTOM)

    entryA = Entry(f1, font="Calibri 26", fg="green", bg="lightblue", width=3)
    entryA.pack(side=LEFT)
    entryA.bind("<FocusOut>", entryColor)  # Добавляем обработку события

    x2 = Label(f1, text="x²", font="Calibri 26", fg="green", padx=10)
    x2.pack(side=LEFT)

    entryB = Entry(f1, font="Calibri 26", fg="green", bg="lightblue", width=3)
    entryB.pack(side=LEFT)
    entryB.bind("<FocusOut>", entryColor)

    x_plus = Label(f1, text="x+", font="Calibri 26", fg="green", padx=10)
    x_plus.pack(side=LEFT)

    entryC = Entry(f1, font="Calibri 26", fg="green", bg="lightblue", width=3)
    entryC.pack(side=LEFT)
    entryC.bind("<FocusOut>", entryColor)

    y = Label(f1, text="= 0", font="Calibri 26", fg="green", padx=10)
    y.pack(side=LEFT)

    btn_lahenda = Button(f1, text="Lahenda", font="calibri 20", fg="green", command=Lahenda)
    btn_lahenda.pack(side=LEFT, padx=5)

    btn_graafik = Button(f1, text="Graafik", font="calibri 20", fg="green", command=Graafik)
    btn_graafik.pack(side=LEFT, padx=5)

    aken.mainloop()


aken()
