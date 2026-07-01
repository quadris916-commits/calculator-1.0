import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Calculator")
        self.root.geometry("360x520")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e1e")

        self.expression = ""

        self.display_var = tk.StringVar()

        self.display = tk.Entry(
            root,
            textvariable=self.display_var,
            font=("Arial", 24),
            bd=10,
            relief=tk.FLAT,
            bg="#2d2d2d",
            fg="white",
            justify="right"
        )
        self.display.pack(fill="both", ipadx=8, ipady=20, padx=10, pady=10)

        buttons_frame = tk.Frame(root, bg="#1e1e1e")
        buttons_frame.pack(expand=True, fill="both", padx=10, pady=10)

        buttons = [
            ["C", "⌫", "%", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["00", "0", ".", "="]
        ]

        for row_index, row in enumerate(buttons):
            buttons_frame.rowconfigure(row_index, weight=1)
            for col_index, button_text in enumerate(row):
                buttons_frame.columnconfigure(col_index, weight=1)

                button = tk.Button(
                    buttons_frame,
                    text=button_text,
                    font=("Arial", 18, "bold"),
                    bd=0,
                    relief=tk.FLAT,
                    command=lambda value=button_text: self.on_button_click(value)
                )

                if button_text in ["+", "-", "*", "/", "=", "%"]:
                    button.configure(bg="#ff9500", fg="white")
                elif button_text in ["C", "⌫"]:
                    button.configure(bg="#a5a5a5", fg="black")
                else:
                    button.configure(bg="#333333", fg="white")

                button.grid(row=row_index, column=col_index, sticky="nsew", padx=5, pady=5)

        self.root.bind("<Return>", lambda event: self.calculate())
        self.root.bind("<BackSpace>", lambda event: self.backspace())
        self.root.bind("<Escape>", lambda event: self.clear())
        self.root.bind("<Key>", self.key_input)

    def on_button_click(self, value):
        if value == "=":
            self.calculate()
        elif value == "C":
            self.clear()
        elif value == "⌫":
            self.backspace()
        else:
            self.expression += value
            self.display_var.set(self.expression)

    def calculate(self):
        try:
            result = str(eval(self.expression))
            self.display_var.set(result)
            self.expression = result
        except ZeroDivisionError:
            self.display_var.set("Cannot divide by zero")
            self.expression = ""
        except Exception:
            self.display_var.set("Error")
            self.expression = ""

    def clear(self):
        self.expression = ""
        self.display_var.set("")

    def backspace(self):
        self.expression = self.expression[:-1]
        self.display_var.set(self.expression)

    def key_input(self, event):
        allowed_keys = "0123456789+-*/.%"
        if event.char in allowed_keys:
            self.expression += event.char
            self.display_var.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()