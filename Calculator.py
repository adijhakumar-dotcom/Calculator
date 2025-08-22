# High-Fi Calculator with GUI
# Author: Aditya Kumar Jha
# Description: A modern calculator with GUI using Tkinter

import tkinter as tk


root = tk.Tk()
root.title("High-Fi Calculator")
root.geometry("400x500")
root.configure(bg="#2C3E50")

expression = ""


def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

def clear():
    global expression
    expression = ""
    equation.set("")

def equal():
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""


equation = tk.StringVar()


entry = tk.Entry(root, textvariable=equation, font=("Arial", 20), bd=10, relief="sunken", justify="right")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8, padx=10, pady=20)


btn_params = {
    "padx": 20,
    "pady": 20,
    "bd": 5,
    "fg": "white",
    "bg": "#34495E",
    "font": ("Arial", 14),
}


buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

for (text, row, col) in buttons:
    if text == "=":
        action = equal
    else:
        action = lambda x=text: press(x)
    tk.Button(root, text=text, command=action, **btn_params).grid(row=row, column=col, padx=5, pady=5)


tk.Button(root, text="C", command=clear, **btn_params).grid(row=5, column=0, columnspan=4, sticky="we", padx=5, pady=10)

root.mainloop()

