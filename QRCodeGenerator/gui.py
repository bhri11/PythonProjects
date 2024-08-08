from tkinter import *
import pyqrcode
from PIL import ImageTk, Image

def generate():
    global image_label  # Global bildirimi fonksiyonun başında olmalıdır

    link_name = name_en.get()
    link = link_en.get()
    file = link_name + ".png"
    url = pyqrcode.create(link)
    url.png(file, scale=8)  # QR kodunu daha büyük oluşturmak için scale değerini artırdık
    image = ImageTk.PhotoImage(Image.open(file).resize((380, 380)))  # Resmi canvas boyutlarına sığacak şekilde yeniden boyutlandırdık

    # Remove previous image if it exists
    if 'image_label' in globals():
        image_label.destroy()

    image_label = Label(root, image=image, bg='white', borderwidth=2, relief="solid")
    image_label.image = image
    image_label.place(x=60, y=350)  # QR kodunu ortalamak için x koordinatını ayarladık

root = Tk()
root.title("QR Code Generator")
root.geometry("500x750")
root.config(bg="lightblue")

title_frame = Frame(root, bg="lightblue")
title_frame.pack(pady=20)

label = Label(title_frame, text="QR Code Generator", fg="red", bg="lightblue", font=("Arial", 24, "bold"))
label.pack()

input_frame = Frame(root, bg="lightblue")
input_frame.pack(pady=20)

name_lab = Label(input_frame, text="Link Name", bg="lightblue", font=("Arial", 14))
name_lab.grid(row=0, column=0, padx=10, pady=10, sticky=E)

name_en = Entry(input_frame, font=("Arial", 14), width=30)
name_en.grid(row=0, column=1, padx=10, pady=10)

link_lab = Label(input_frame, text="Link", bg="lightblue", font=("Arial", 14))
link_lab.grid(row=1, column=0, padx=10, pady=10, sticky=E)

link_en = Entry(input_frame, font=("Arial", 14), width=30)
link_en.grid(row=1, column=1, padx=10, pady=10)

button_frame = Frame(root, bg="lightblue")
button_frame.pack(pady=20)

button = Button(button_frame, text="Generate QR Code", font=("Arial", 14, "bold"), bg="green", fg="white", command=generate)
button.pack()

canvas_frame = Frame(root, bg="lightblue")
canvas_frame.pack(pady=20)

canvas = Canvas(canvas_frame, width=400, height=400, bg="white", borderwidth=2, relief="solid")
canvas.pack()

root.mainloop()
