from tkinter import *

window = Tk()

FONT = ("arial", 30)
input_text: str = ""
text_str = StringVar

special_symbols = {"\u00F7": "/", "\u00D7": "*"}

def write(number: str) -> None:
    global input_text
    input_text += str(number)
    label.config(text=input_text)


def output(special_symbols) -> None:
    global input_text
    for key in special_symbols.keys():
        if key in input_text:
            input_change = input_text.replace(key, special_symbols[key])
            input_text = input_change
    label.config(text=str(eval(input_text)))
    input_text = str(eval(input_text))


def clear() -> None:
    global input_text
    input_text = ""
    label.config(text="")


def exponentiation() -> None:
    global input_text
    input_text = str(float(input_text)**2)
    label.config(text=input_text)


def elementalization() -> None:
    global input_text
    input_text = str(float(input_text)**(1/2))
    label.config(text=input_text)


window.title("Calculator")
window.geometry("375x667")

icon = PhotoImage(file="icon.png")
window.iconphoto(True, icon)

label = Label(window, font=FONT)
label.grid(row=0, column=0, columnspan=3)


Button(window, text="C", font=FONT, bd=0, command=clear).grid(row=2, column=0)
Button(window, text="x\u00b2", font=FONT, bd=0, command=exponentiation).grid(row=2, column=1)
Button(window, text="\u221ax", font=FONT, bd=0, command=elementalization).grid(row=2, column=2)


numbers = {".": (6, 0), "0": (6, 1),
           "1": (5, 0), "2": (5, 1), "3": (5, 2), "+": (5, 3),
           "4": (4, 0), "5": (4, 1), "6": (4, 2), "-": (4, 3),
           "7": (3, 0), "8": (3, 1), "9": (3, 2), "\u00D7": (3, 3),
           "\u00F7": (2, 3)
           }

for keys, values in numbers.items():
    Button(window, text=keys, font=FONT, bd=0, command=lambda x=keys: write(x)).grid(row=values[0], column=values[1])


Button(window, text="=",
       font=("arial", 30),
       bd=0,
       command=lambda: output(special_symbols)).grid(row=6, column=2, columnspan=3)

window.mainloop()
