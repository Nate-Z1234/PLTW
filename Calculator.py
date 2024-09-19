import customtkinter as ctk
import sys
import random
from enum import Enum

#Calculator
class Calculator(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Calculator")
        self.geometry("450x520")

        self.expression = ""
        self.input_text = ctk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        input_frame = ctk.CTkFrame(self, width=400, height=50)
        input_frame.pack(side=ctk.TOP)

        input_field = ctk.CTkEntry(input_frame, textvariable=self.input_text, width=450, height=55, font=('Courier', 18, 'bold'), justify=ctk.RIGHT)
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=10)

        btns_frame = ctk.CTkFrame(self, width=350, height=350)
        btns_frame.pack()

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+',
            ' ', ' ', ' ', ' '
        ]

        row = 0
        col = 0
        for button in buttons:
            btn = ctk.CTkButton(btns_frame, text=button, width=100, height=100, command=lambda b=button: self.on_button_click(b))
            btn.grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def on_button_click(self, button):
        if button == "C":
            self.expression = ""
            self.input_text.set("")
        elif button == "=":
            try:
                result = str(eval(self.expression))
                self.input_text.set(result)
                self.expression = result
            except:
                self.input_text.set("error...")
                self.expression = ""
        elif button == " ":
            self.expression = ""
            self.input_text.set("Secret Found...")
            self.destroy()

            #Counter Click (TWIST🤣)
            class ClickCounterApp:
                def __init__(self, root):
                    self.root = root
                    self.root.title("Click Counter")
                    self.root.geometry("500x200")
        
                    self.click_count = 0
                    self.colors = ["#5afaa5", "#5afadd", "#5aedfa", "#5ac2fa", "#5a97fa", "#975afa"]
        
                    self.button = ctk.CTkButton(root, text="Click me!", font=('Courier', 18, 'bold'), command=self.on_click)
                    self.button.pack(pady=20)
        
                    self.label = ctk.CTkLabel(root, text="Button clicked 0 times", font=('Courier', 18, 'bold'))
                    self.label.pack(pady=10)
        
                def on_click(self):
                    self.click_count += 1
                    new_color = self.colors[self.click_count % len(self.colors)]
                    self.button.configure(fg_color=new_color)
                    self.root.configure(bg=new_color)
                    self.label.configure(text=f"Button clicked {self.click_count} times")

            if __name__ == "__main__":
                root = ctk.CTk()
                app = ClickCounterApp(root)
                root.mainloop()

        else:
            self.expression += button
            self.input_text.set(self.expression)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop() #lol I got 100 lines of code 🫠🫠🫠