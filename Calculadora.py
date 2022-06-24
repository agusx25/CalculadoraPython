import tkinter as tk

from tkinter import ttk
import random


class Calculadora():
    def __init__(self):

        root = tk.Tk()
        root.columnconfigure(0, weight=1)
        root.columnconfigure(1, weight=3)
        self.labelResultado = tk.StringVar()
        self.frm = ttk.Frame(root, padding=10)
        self.frm.grid()
        self.ttkLabel = ttk.Entry(self.frm, textvariable=self.labelResultado, width=40)
        self.ttkLabel.grid(column=0, row=0, columnspan=4, sticky="nsew")
        self.operators = ['+', '-', '*', '/']
        # generar botones

        for i in range(len(self.operators)):
            ttk.Button(self.frm, text=self.operators[i], command=lambda i=i: self.add_numbers(self.operators[i])).grid(column=i, row=1,  pady = 20, sticky="nsew")
        b= ttk.Button(self.frm, text='=', command=self.solve_equation)
        b.grid( column=4, row=1, rowspan=2) 
        root.mainloop()
        
    def add_numbers(self, number):
        resultado = self.labelResultado.get()

        self.labelResultado.set(resultado + number)
        self.ttkLabel.focus_set()
        self.ttkLabel.icursor(len(resultado)+1)

    def solve_equation(self):
        try:
            self.labelResultado.set(eval(self.labelResultado.get()))
        except SyntaxError:
            self.labelResultado.set("Error de sintaxis")
        except ZeroDivisionError:
            pass


calculadora = Calculadora()
