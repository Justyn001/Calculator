from tkinter import *

window = Tk()

FONT = ("arial", 30)
input_text: str = ""


def write(number: str) -> None:
    global input_text
    input_text += str(number)
    label.config(text=input_text)


def output() -> None:
    global input_text
    label.config(text=str(eval(input_text)))
    input_text = str(eval(input_text))


def clear() -> None:
    global input_text
    input_text = ""
    label.config(text="")


window.title("Calculator")
window.geometry("375x667")

icon = PhotoImage(file="icon.png")
window.iconphoto(True, icon)

label = Label(window, font=FONT)
label.grid(row=0, column=0, columnspan=3)


Button(window, text="C", font=FONT, bd=0, command=clear).grid(row=2, column=0)
Button(window, text="x\u00b2", font=FONT, bd=0).grid(row=2, column=1)
Button(window, text="\u221ax", font=FONT, bd=0).grid(row=2, column=2)
Button(window, text="\u00F7", font=FONT, bd=0).grid(row=2, column=3)
Button(window, text="\u00D7", font=FONT, bd=0).grid(row=3, column=3)
Button(window, text="-", font=FONT, bd=0, command=lambda: write("-")).grid(row=4, column=3)
Button(window, text="+", font=FONT, bd=0, command=lambda: write("+")).grid(row=5, column=3)

Button(window, text="7", font=FONT, bd=0, command=lambda: write("7")).grid(row=3, column=0)
Button(window, text="8", font=FONT, bd=0, command=lambda: write("8")).grid(row=3, column=1)
Button(window, text="9", font=FONT, bd=0, command=lambda: write("9")).grid(row=3, column=2)
Button(window, text="4", font=FONT, bd=0, command=lambda: write("4")).grid(row=4, column=0)
Button(window, text="5", font=FONT, bd=0, command=lambda: write("5")).grid(row=4, column=1)
Button(window, text="6", font=FONT, bd=0, command=lambda: write("6")).grid(row=4, column=2)
Button(window, text="1", font=FONT, bd=0, command=lambda: write("1")).grid(row=5, column=0)
Button(window, text="2", font=FONT, bd=0, command=lambda: write("2")).grid(row=5, column=1)
Button(window, text="3", font=FONT, bd=0, command=lambda: write("3")).grid(row=5, column=2)
Button(window, text=".", font=FONT, bd=0, command=lambda: write(".")).grid(row=6, column=0)
Button(window, text="0", font=FONT, bd=0, command=lambda: write("0")).grid(row=6, column=1)

Button(window, text="=",
       font=("arial", 30),
       bd=0,
       command=output).grid(row=6, column=2, columnspan=3)

window.mainloop()
