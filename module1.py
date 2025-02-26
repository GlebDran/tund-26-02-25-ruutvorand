import smtplib
import ssl
import imghdr
from email.message import EmailMessage
import tkinter as tk
from tkinter import Entry, Text, Button, Label, filedialog, messagebox, PhotoImage

def vali_pilt():
    file = filedialog.askopenfilename()
    attach_entry.delete(0, tk.END)  # Очистить поле ввода
    attach_entry.insert(0, file)  # Вставить путь к файлу

def saada_kiri():
    kellele = email_entry.get()
    teema = subject_entry.get()
    kiri = message_text.get("1.0", tk.END).strip()
    failitee = attach_entry.get()

    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "glebdranitsyn@gmail.com"
    password = "oeid ycrk uwit tnpk"

    if not kellele or not kiri:
        messagebox.showerror("Viga", "Palun sisestage e-posti aadress ja kiri!")
        return

    msg = EmailMessage()
    msg.set_content(kiri)
    msg['Subject'] = teema
    msg['From'] = sender_email
    msg['To'] = kellele

    if failitee:
        try:
            with open(failitee, 'rb') as fpilt:
                pilt = fpilt.read()
            msg.add_attachment(pilt, maintype='image', subtype=imghdr.what(None, pilt))
        except Exception as e:
            messagebox.showerror("Viga", f"Faili lisamine ebaõnnestus: {e}")
            return

    try:
        context = ssl.create_default_context()
        server = smtplib.SMTP(smtp_server, port)
        server.starttls(context=context)
        server.login(sender_email, password)
        server.send_message(msg)
        server.quit()
        messagebox.showinfo("Informatsioon", "Kiri saadetud edukalt!")
    except Exception as e:
        messagebox.showerror("Tekkis viga!", f"Viga: {e}")

# Гл окно
root = tk.Tk()
root.title("E-kirja saatmine")
root.configure(bg="white")
root.geometry("500x350")
icon = PhotoImage(file="logo1.png")
root.iconphoto(True, icon)

#цвета
bg_color = "blue"
fg_color = "white"
btn_color = "darkblue"
btn_fg = "white"

#метки
labels = ["EMAIL:", "TEEMA:", "LISA:", "KIRI:"]
for i, text in enumerate(labels):
    label = Label(root, text=text, bg=bg_color, fg=fg_color, font=("Arial", 12, "bold"), width=10, anchor="w")
    label.grid(row=i, column=0, padx=5, pady=5, sticky="nsew")

#поля ввода
email_entry = Entry(root, width=40)
email_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

subject_entry = Entry(root, width=40)
subject_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

attach_entry = Entry(root, width=40)
attach_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

message_text = Text(root, width=40, height=8)
message_text.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

#кнопки
add_image_btn = Button(root, text="LISA PILT", bg=btn_color, fg=btn_fg, font=("Arial", 12, "bold"), command=vali_pilt)
add_image_btn.grid(row=4, column=0, padx=5, pady=5, sticky="ew")

send_btn = Button(root, text="SAADA", bg=btn_color, fg=btn_fg, font=("Arial", 12, "bold"), command=saada_kiri)
send_btn.grid(row=4, column=1, padx=5, pady=5, sticky="ew")

#размер колонок
root.columnconfigure(1, weight=1)

root.mainloop()
