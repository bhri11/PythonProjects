from tkinter import *
from tkinter import font
import ast

#my First GitHub project
root = Tk()
i = 0


def get_number(num):
    global i
    display.insert(i, num)
    i += 1


def get_operation(operator):
    global i
    length = len(operator)
    display.insert(i, operator)
    i += length


def clear_all():
    display.delete(0,END)


def calculate():
    entire_string = display.get()
    try:
        node = ast.parse(entire_string, mode="eval")
        result = eval(compile(node, "<string>", "eval"))
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0,"Error")


def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0, new_string)
    else:
        clear_all()
        display.insert(0, "")

display = Entry(root, width=30, font=('Helvetica', 16))
display.grid(row=1, columnspan=6, padx=10, pady=10)

my_font = font.Font(family='Helvetica', size=12, weight='bold')


numbers = [1,2,3,4,5,6,7,8,9]
counter = 0
for x in range(3):
    for y in range(3):
        button_text = numbers[counter]
        button = Button(root, text=button_text, font=my_font, bg='#4CAF50', fg='#FFFFFF', width=5, height=2,
                        command=lambda text=button_text: get_number(text))
        button.grid(row=x+2, column=y, padx=5, pady=5)
        counter += 1

button = Button(root, text=0, font=my_font, bg='#4CAF50', fg='#FFFFFF', width=5, height=2,command=lambda: get_number(0))
button.grid(row=5, column=1, padx=5, pady=5)

operator_count = 0
operations = ["+", "-", "*", "/", "*3.14", "%", "(", ")", "**", "**2"]
for x in range(4):
    for y in range(3):
        if operator_count<len(operations):
            button = Button(root, text=operations[operator_count], font=my_font, bg='#FF5722', fg='#FFFFFF', width=5,
                            height=2, command=lambda text=operations[operator_count]: get_operation(text))
            button.grid(row=x + 2, column=y + 3, padx=5, pady=5)
            operator_count += 1

button = Button(root, text="AC", font=my_font, bg='#4CAF50', fg='#FFFFFF', width=5, height=2,command=clear_all)
button.grid(row=5, column=0, padx=5, pady=5)

button = Button(root, text="=", font=my_font, bg='#4CAF50', fg='#FFFFFF', width=5, height=2,command=calculate)
button.grid(row=5, column=2, padx=5, pady=5)

button = Button(root, text="<-", font=my_font, bg='#0000FF', fg='#FFFFFF', width=5, height=2,command=undo)
button.grid(row=5, column=4, padx=5, pady=5)

button = Button(root, text=".", font=my_font, bg='#4CAF50', fg='#FFFFFF', width=5, height=2, command=lambda: get_operation("."))
button.grid(row=5, column=5, padx=5, pady=5)
root.mainloop()
