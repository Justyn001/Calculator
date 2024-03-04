from tkinter import *

FONT = ("arial", 30)


class Calculator:

    def __init__(self) -> None:
        self.window = Tk()
        self.window.title("Calculator")
        self.window.resizable(None, None)

        self.text: str = "siema"

        self.frame_labels = self.create_frame()
        self.frame_buttons = self.create_frame()

        self.label_one = self.create_display_label()
        self.label_two = self.create_display_label()

        self.buttons = {"7": (3, 0), "8": (3, 1), "9": (3, 2),
                        "4": (4, 0), "5": (4, 1), "6": (4, 2),
                        "1": (5, 0), "2": (5, 1), "3": (5, 2),
                        ".": (6, 0), "0": (6, 1)}

        self.special_buttons = {"\u00F7": "/", "\u00D7": "*", "-": "-", "+": "+"}

        self.create_buttons()
        self.create_operations()
        self.create_clear()
        self.create_x_2()
        self.create_x_sqrt()
        self.create_equal()

    def create_frame(self):
        frame = Frame(self.window, bg="pink")
        frame.pack(fill='both')
        return frame

    def create_display_label(self):
        label = Label(self.frame_labels, text=self.text, bg="pink", font=FONT, padx=5, pady=5, anchor=E)
        label.pack(fill='both')
        return label

    def create_buttons(self) -> None:
        for numbers, cords in self.buttons.items():
            Button(self.frame_buttons, text=numbers, font=FONT, bd=0, bg="red",
                   command=lambda x=numbers: self.write(x)).grid(row=cords[0], column=cords[1], sticky=NSEW)

    def create_operations(self) -> None:
        row = 2
        for symbol, operation in self.special_buttons.items():
            Button(self.frame_buttons, text=symbol, font=FONT, bd=0, bg="green",
                   command=lambda x=operation: self.write(operation)).grid(row=row, column=3, sticky=NSEW)
            row += 1

    def create_clear(self):
        Button(self.frame_buttons, text="C", font=FONT, bd=0, bg="green",
               command=lambda: self.clear()).grid(row=2, column=0)

    def create_x_2(self):
        Button(self.frame_buttons, text="x\u00b2", font=FONT, bd=0, bg="green",
               command=lambda: self.x_to_2()).grid(row=2, column=1)

    def create_x_sqrt(self):
        Button(self.frame_buttons, text="\u221ax", font=FONT, bd=0, bg="green",
               command=lambda: self.x_sqrt()).grid(row=2, column=2)

    def create_equal(self):
        Button(self.frame_buttons, text="=", font=FONT, bd=0, bg="blue",
               command=lambda: self.equal()).grid(row=6, column=2, columnspan=3, sticky=NSEW)

    def write(self, x: str) -> None:
        pass

    def clear(self):
        pass

    def x_to_2(self):
        pass

    def x_sqrt(self):
        pass

    def equal(self):
        pass

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()

# from tkinter import *
#
# window = Tk()
#
# FONT = ("arial", 30)
# input_text: str = ""
# window.resizable(0, 0)
#
# special_symbols = {"\u00F7": "/", "\u00D7": "*"}
#
#
# def write(number: str) -> None:
#     global input_text
#     input_text += str(number)
#     label.config(text=input_text)
#
#
# def output(special_symbols) -> None:
#     global input_text
#     for key in special_symbols.keys():
#         if key in input_text:
#             input_change = input_text.replace(key, special_symbols[key])
#             input_text = input_change
#     label.config(text=str(eval(input_text)))
#     input_text = str(eval(input_text))
#
#
# def clear() -> None:
#     global input_text
#     input_text = ""
#     label.config(text="")
#
#
# def exponentiation() -> None:
#     global input_text
#     input_text = str(float(input_text)**2)
#     label.config(text=input_text)
#
#
# def elementalization() -> None:
#     global input_text
#     input_text = str(float(input_text)**(1/2))
#     label.config(text=input_text)
#
#
# window.title("Calculator")
# window.geometry("375x667")
#
# icon = PhotoImage(file="icon.png")
# window.iconphoto(True, icon)
#
# label = Label(window, font=FONT)
# label.grid(row=0, column=0, columnspan=3)
#
# Button(window, text="C", font=FONT, bd=0, command=clear).grid(row=2, column=0)
# Button(window, text="x\u00b2", font=FONT, bd=0, command=exponentiation).grid(row=2, column=1)
# Button(window, text="\u221ax", font=FONT, bd=0, command=elementalization).grid(row=2, column=2)
#
# numbers = {".": (6, 0), "0": (6, 1),
#            "1": (5, 0), "2": (5, 1), "3": (5, 2), "+": (5, 3),
#            "4": (4, 0), "5": (4, 1), "6": (4, 2), "-": (4, 3),
#            "7": (3, 0), "8": (3, 1), "9": (3, 2), "\u00D7": (3, 3),
#            "\u00F7": (2, 3)
#            }
#
# for keys, values in numbers.items():
#     Button(window, text=keys, font=FONT, bd=0, command=lambda x=keys: write(x)).grid(row=values[0], column=values[1])
#
#
# Button(window, text="=",
#        font=("arial", 30),
#        bd=0,
#        command=lambda: output(special_symbols)).grid(row=6, column=2, columnspan=3)
#
# window.mainloop()
