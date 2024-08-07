import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Simple Calculator")
        self.window.geometry("400x500")  # Set a fixed size for the window
        self.center_window()  # Center the window
        self.entry1 = tk.Entry(self.window, width=20, font=("Arial", 18))
        self.entry2 = tk.Entry(self.window, width=20, font=("Arial", 18))
        self.result_label = tk.Label(self.window, text="Result:", font=("Arial", 18))
        self.history_label = tk.Label(self.window, text="History:", font=("Arial", 18))
        self.history_text = tk.Text(self.window, height=10, width=40, font=("Arial", 12))

        self.create_widgets()

    def center_window(self):
        self.window.update_idletasks()
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def create_widgets(self):
        tk.Label(self.window, text="Number 1:", font=("Arial", 18)).grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.entry1.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.window, text="Number 2:", font=("Arial", 18)).grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.entry2.grid(row=1, column=1, padx=10, pady=10)

        tk.Button(self.window, text="Add", command=self.add, font=("Arial", 18)).grid(row=2, column=0, padx=10, pady=10)
        tk.Button(self.window, text="Subtract", command=self.subtract, font=("Arial", 18)).grid(row=2, column=1, padx=10, pady=10)
        tk.Button(self.window, text="Multiply", command=self.multiply, font=("Arial", 18)).grid(row=3, column=0, padx=10, pady=10)
        tk.Button(self.window, text="Divide", command=self.divide, font=("Arial", 18)).grid(row=3, column=1, padx=10, pady=10)

        self.result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        tk.Button(self.window, text="History", command=self.show_history, font=("Arial", 18)).grid(row=5, column=0, padx=10, pady=10)
        tk.Button(self.window, text="Clear", command=self.clear, font=("Arial", 18)).grid(row=5, column=1, padx=10, pady=10)
        
        self.history_label.grid(row=6, column=0, columnspan=2, padx=10, pady=10)
        self.history_text.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

    def add(self):
        try:
            num1 = float(self.entry1.get())
            num2 = float(self.entry2.get())
            result = num1 + num2
            self.result_label.config(text=f"Result: {result}")
            self.save_history(f"Added {num1} and {num2}. Result: {result}")
        except ValueError:
            messagebox.showerror("Error", "Invalid input")

    def subtract(self):
        try:
            num1 = float(self.entry1.get())
            num2 = float(self.entry2.get())
            result = num1 - num2
            self.result_label.config(text=f"Result: {result}")
            self.save_history(f"Subtracted {num2} from {num1}. Result: {result}")
        except ValueError:
            messagebox.showerror("Error", "Invalid input")

    def multiply(self):
        try:
            num1 = float(self.entry1.get())
            num2 = float(self.entry2.get())
            result = num1 * num2
            self.result_label.config(text=f"Result: {result}")
            self.save_history(f"Multiplied {num1} and {num2}. Result: {result}")
        except ValueError:
            messagebox.showerror("Error", "Invalid input")

    def divide(self):
        try:
            num1 = float(self.entry1.get())
            num2 = float(self.entry2.get())
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero")
            else:
                result = num1 / num2
                self.result_label.config(text=f"Result: {result}")
                self.save_history(f"Divided {num1} by {num2}. Result: {result}")
        except ValueError:
            messagebox.showerror("Error", "Invalid input")

    def save_history(self, text):
        with open("history.txt", "a") as file:
            file.write(text + "\n")

    def show_history(self):
        try:
            with open("history.txt", "r") as file:
                self.history_text.delete(1.0, tk.END)
                self.history_text.insert(tk.END, file.read())
        except FileNotFoundError:
            self.history_text.delete(1.0, tk.END)
            self.history_text.insert(tk.END, "No history available")

    def clear(self):
        self.entry1.delete(0, tk.END)
        self.entry2.delete(0, tk.END)
        self.result_label.config(text="Result:")

if __name__ == "__main__":
    calculator = Calculator()
    calculator.window.mainloop()
