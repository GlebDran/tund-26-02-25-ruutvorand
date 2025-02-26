from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
from tkinter import messagebox

# Глобальные переменные для хранения корней
roots = []
has_solution = False

def Solve():
    global roots, has_solution
    roots = []
    has_solution = False
    
    try:
        a = float(entryA.get())
        b = float(entryB.get())
        c = float(entryC.get())

        if a == 0:  # Проверяем, чтобы a не было равно 0
            messagebox.showerror("Ошибка", "Коэффициент 'a' не может быть 0.")
            return

        D = b**2 - 4 * a * c

        if D > 0:
            x1 = round((-b + (D ** 0.5)) / (2 * a), 2)
            x2 = round((-b - (D ** 0.5)) / (2 * a), 2)
            label5.configure(text=f"D > 0 --> 2 решения: \n x1 = {x1}\n x2 = {x2}")
            roots = [x1, x2]
            has_solution = True

        elif D == 0:
            x = round(-b / (2 * a), 2)
            label5.configure(text=f"D = 0 --> 1 решение: \n x = {x}")
            roots = [x]
            has_solution = True

        else:
            label5.configure(text="Решений нет")

    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные числовые значения!")


def Graafik():
    global roots, has_solution
    if not has_solution:
        messagebox.showerror("Ошибка", "Решение ещё не найдено!")
        return

    a = float(entryA.get())
    b = float(entryB.get())
    c = float(entryC.get())

    if len(roots) == 2:
        x1, x2 = roots
        x_range = max(abs(x1), abs(x2)) + 2
    else:
        x_range = 10

    x = np.linspace(-x_range, x_range, 100)
    y = a * x**2 + b * x + c

    plt.plot(x, y, label=f"{a}x² + {b}x + {c}")
    plt.axhline(0, color="black", linewidth=0.5)
    plt.axvline(0, color="black", linewidth=0.5)
    plt.grid()
    plt.legend()
    plt.show()


def entryColor(event):
    event.widget.configure(bg="red" if event.widget.get().strip() == "" else "#ffe6f0")


def aken():
    global entryA, entryB, entryC, label5

    aken = Tk()
    aken.geometry("800x260")
    aken.resizable(False, False)
    aken.title("Ruutvõrrand")

    # Загрузка изображения
    try:
        original_image = Image.open(r"image.jpg")
        resized_image = original_image.resize((800, 260))
        bgimage = ImageTk.PhotoImage(resized_image)
        labelBG = Label(aken, image=bgimage)
        labelBG.place(x=0, y=0)
    except Exception as e:
        print("Ошибка загрузки изображения:", e)

    # Фрейм для элементов
    f1 = Frame(aken, width=800, height=260, bg="lightblue")
    f1.place(relx=0.5, rely=0.5, anchor=CENTER)

    lbl = Label(f1, text="Ruutvõrrandite lahendamine", font="Calibri 26", fg="green", bg="lightblue")
    lbl.pack(side=TOP)

    entryA = Entry(f1, font="Calibri 26", fg="green", bg="lightblue", width=3)
    entryA.pack(side=LEFT)
    entryA.bind("<FocusOut>", entryColor)

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

    btn_lahenda = Button(f1, text="Lahenda", font="calibri 20", fg="green", command=Solve)
    btn_lahenda.pack(side=LEFT, padx=5)

    btn_graafik = Button(f1, text="Graafik", font="calibri 20", fg="green", command=Graafik)
    btn_graafik.pack(side=LEFT, padx=5)

    label5 = Label(f1, text="", font="Calibri 16", fg="black", bg="lightblue")
    label5.pack(side=BOTTOM)

    aken.mainloop()


aken()
