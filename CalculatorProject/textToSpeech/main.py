from gtts import gTTS
import os
from tkinter import *

# text = open("demo.txt", "r").read()
# language = "en"
#
# output = gTTS(text=text, lang=language, slow=False)
# output.save("fileoutput.mp3")
# os.system("start fileoutput.mp3")

def textToSpeech():
    text = entry.get()
    language = languages[language_var.get()]
    output = gTTS(text=text, lang=language, slow=False)
    output.save("output.mp3")
    os.system("start output.mp3")

root = Tk()
root.title("Text to Speech")
root.geometry("400x300")
root.configure(bg="#f0f0f0")

canvas = Canvas(root, width=400, height=300, bg="#f0f0f0", highlightthickness=0)
canvas.pack()

label = Label(root, text="Enter Text:", font=("Arial", 14), bg="#f0f0f0")
canvas.create_window(200, 120, window=label)

entry = Entry(root, font=("Arial", 14), width=30, bd=2, relief="groove")
canvas.create_window(200, 150, window=entry)

language_label = Label(root, text="Select Language:", font=("Arial", 12), bg="#f0f0f0")
canvas.create_window(200, 190, window=language_label)

language_var = StringVar(root)
language_var.set("English")  # default value

languages = {"English": "en", "French": "fr", "Spanish": "es", "German": "de", "Italian": "it", "Turkish": "tr"}
language_menu = OptionMenu(root, language_var, *languages.keys())
canvas.create_window(200, 220, window=language_menu)

button = Button(root, text="Start", command=textToSpeech, font=("Arial", 12), bg="#4CAF50", fg="white", bd=0, padx=10, pady=5, activebackground="#45a049")
canvas.create_window(200, 260, window=button)

root.mainloop()