from tkinter import *

FONT_BUTTONS = ("arial", 24, "bold")
FONT_SPECIAL = ("arial", 20)
FONT_LABEL = ("arial", 30, "bold")
FONT_LABEL_2 = ("arial", 24)

LABEL_COLOUR = "#edede6"
BUTTONS_COLOUR = "#f7f7f2"
SPECIAL_BUTTONS_COLOUR = "#c9f2db"
EQUAL_COLOUR = "#E4EFF0"


class Calculator:

    def __init__(self) -> None:
        self.window = Tk()
        self.window.title("Calculator")
        self.window.geometry("375x667")
        self.window.resizable(None, None)

        self.text: str = ""
        self.output: str = ""

        self.frame_labels = self.create_frame_label()
        self.frame_buttons = self.create_frame_buttons()

        self.label_two, self.label_one = self.create_display_label()

        for i in range(0, 4):
            self.frame_buttons.rowconfigure(i, weight=1)
            self.frame_buttons.columnconfigure(i, weight=1)

        self.buttons = {"7": (1, 0), "8": (1, 1), "9": (1, 2),
                        "4": (2, 0), "5": (2, 1), "6": (2, 2),
                        "1": (3, 0), "2": (3, 1), "3": (3, 2),
                        ".": (4, 0), "0": (4, 1)}

        self.special_buttons = {"\u00F7": "/", "\u00D7": "*", "-": "-", "+": "+"}

        self.create_buttons()
        self.create_operations()
        self.create_clear()
        self.create_x_2()
        self.create_x_sqrt()
        self.create_equal()

    def create_frame_label(self):
        frame = Frame(self.window, bg="pink")
        frame.pack(fill='both', expand=True)
        return frame

    def create_frame_buttons(self):
        frame = Frame(self.window, bg=SPECIAL_BUTTONS_COLOUR)
        frame.pack(fill='both', expand=True)
        return frame

    def create_display_label(self):
        label_two = Label(self.frame_labels, text=self.text, bg=LABEL_COLOUR, font=FONT_LABEL_2, padx=10, pady=5,
                          anchor=E)
        label_two.pack(fill='both', expand=True)

        label_one = Label(self.frame_labels, text=self.text, bg=LABEL_COLOUR, font=FONT_LABEL, padx=5, pady=5, anchor=E)
        label_one.pack(fill='both', expand=True)

        return label_two, label_one

    def create_buttons(self) -> None:
        for numbers, cords in self.buttons.items():
            (Button(self.frame_buttons, text=numbers, font=FONT_BUTTONS, bd=0, bg=BUTTONS_COLOUR,
                    activebackground=BUTTONS_COLOUR, command=lambda x=numbers: self.write(x))
             .grid(row=cords[0], column=cords[1], sticky=NSEW))

    def create_operations(self) -> None:
        row = 0
        for symbol, operation in self.special_buttons.items():
            (Button(self.frame_buttons, text=symbol, font=FONT_SPECIAL, bd=0, bg=SPECIAL_BUTTONS_COLOUR,
                    activebackground=SPECIAL_BUTTONS_COLOUR, command=lambda x=symbol: self.write(x))
             .grid(row=row, column=3, sticky=NSEW))
            row += 1

    def create_clear(self) -> None:
        Button(self.frame_buttons, text="C", font=FONT_SPECIAL, bd=0, bg=SPECIAL_BUTTONS_COLOUR,
               activebackground=SPECIAL_BUTTONS_COLOUR, command=lambda: self.clear()).grid(row=0, column=0)

    def create_x_2(self) -> None:
        Button(self.frame_buttons, text="x\u00b2", font=FONT_SPECIAL, bd=0, bg=SPECIAL_BUTTONS_COLOUR,
               activebackground=SPECIAL_BUTTONS_COLOUR, command=lambda: self.x_to_2()).grid(row=0, column=1)

    def create_x_sqrt(self) -> None:
        Button(self.frame_buttons, text="\u221ax", font=FONT_SPECIAL, bd=0, bg=SPECIAL_BUTTONS_COLOUR,
               activebackground=SPECIAL_BUTTONS_COLOUR, command=lambda: self.x_sqrt()).grid(row=0, column=2)

    def create_equal(self) -> None:
        Button(self.frame_buttons, text="=", font=FONT_SPECIAL, bd=0, bg=EQUAL_COLOUR, activebackground=EQUAL_COLOUR,
               command=lambda: self.equal()).grid(row=4, column=2, columnspan=3, sticky=NSEW)

    def write(self, x: str) -> None:
        self.text += x
        self.label_one.config(text=self.text)

    def clear(self) -> None:
        self.text = ""
        self.text = ""
        self.label_one.config(text=self.text)
        self.label_two.config(text=self.text)

    def x_to_2(self) -> None:
        self.text = str(float(self.text) ** 2)
        self.label_one.config(text=self.text)

    def x_sqrt(self) -> None:
        self.text = str(float(self.text) ** (1 / 2))
        self.label_one.config(text=self.text)

    def equal(self) -> None:
        self.output = self.text
        for symbol, operation in self.special_buttons.items():
            if symbol in self.text:
                self.text = self.text.replace(symbol, operation)
        self.text = str(eval(self.text))
        self.label_one.config(text=self.text)
        self.label_two.config(text=self.output)

    def run(self) -> None:
        self.window.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()
