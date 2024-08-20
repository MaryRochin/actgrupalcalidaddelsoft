import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    """
    Aplicación de calculadora simple que realiza operaciones básicas y funciones 
    matemáticas como raíz cuadrada y exponencial.

    by:
    - Mariana Guadaluper Lopez Rochin
    - Jose Vega
    - Alexandra Gomez
    -Nery
    
    """
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        self.entry = tk.Entry(root, width=16, font=('Arial', 24), bd=8, insertwidth=2, justify='right')
        self.entry.grid(row=0, column=0, columnspan=4)

        self.create_buttons()

    def create_buttons(self):
        """
        En esta función se crean los botones de la calculadora y se les asigna 
        la función click_event para que realicen la acción correspondiente al 
        ser presionados.
        """
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            '√', 'exp', 'C'
        ]

        row = 1
        col = 0
        for button in buttons:
            action = lambda x=button: self.click_event(x)
            tk.Button(self.root, text=button, width=10, height=3, command=action).grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def click_event(self, key):
        """
        Esta función realiza la acción correspondiente al botón que haya sido presionado 
        por el usuario.
        """
        if key == '=':
            try:
                result = str(eval(self.entry.get()))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")
        elif key == 'C':
            self.clear_entry()
        elif key == '√':
            try:
                num = float(self.entry.get())
                result = self.sqrt_approximation(num)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")
        elif key == 'exp':
            try:
                num = float(self.entry.get())
                result = self.exp_approximation(num)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")
        else:
            self.entry.insert(tk.END, key)

    def sqrt_approximation(self, num):
        """
        Esta función calcula la raíz cuadrada de un número, se redondea 
        el valor a 3 decimales, como se indica en la actividad.
        """
        x = num
        root = 0.5 * (x + (num / x))
        while abs(root - x) >= 0.001:
            x = root
            root = 0.5 * (x + (num / x))
        return round(root, 3)

    def exp_approximation(self, x, terms=10):
        """
        Esta función calcula la exponencial de un número, se redondea el 
        valor a 3 decimales,
        """
        result = 1
        factorial = 1
        power = 1
        for i in range(1, terms):
            factorial *= i
            power *= x
            result += power / factorial
        return round(result, 3)

    def clear_entry(self):
        """
        Esta función limpia la entrada de la calculadora.
        """
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
