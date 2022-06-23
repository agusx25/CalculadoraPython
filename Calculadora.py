import tkinter as tk

from tkinter import ttk
import random


class Calculadora():
    def __init__(self):
        # def changeText(numero):

        #     text.set(str(numero))
        # gui = tk.Tk()
        # gui.geometry('300x100')
        #resultado = ttk.StringVar()
        # text.set('Hola pete')

        # label = tk.Label(gui, textvariable=text)
        # label.pack(pady=50)

        # button = tk.Button(gui, text='hola pete', command= lambda :  changeText(random.randint(0,100)))
        # button.pack()
        # gui.mainloop()
        root = tk.Tk()
        self.labelResultado = tk.StringVar()
        self.labelResultado.set('0')
        self.frm = ttk.Frame(root, padding=10)
        self.frm.grid()
        self.ttkLabel = ttk.Label(self.frm, textvariable=self.labelResultado).grid(column=4, row=0)
        self.operators = ['+', '-', '*', '/']
        # generar botones
        for i in range(1, 10):
            column = i-3 * ((i-1)//3)
            row = (i+2)//3
            ttk.Button(self.frm, text=i, command=lambda i=i: self.add_numbers(str(i))).grid(column=column, row=row) 

            
        for i in range(len(self.operators)):
            ttk.Button(self.frm, text=self.operators[i], command=lambda i=i: self.add_numbers(self.operators[i])).grid(column=4, row=i+1)
        ttk.Button(self.frm, text='=', command=self.solve_equation).grid( column=4, row=5)
        root.mainloop()
        
    def add_numbers(self, number):
        resultado = self.labelResultado.get()
        if resultado == '0':
            self.labelResultado.set(number)
        else:
            self.labelResultado.set(resultado + number)

    def solve_equation(self):
        try:
            self.labelResultado.set(eval(self.labelResultado.get()))

        except SyntaxError:
            self.labelResultado.set("Error de sintaxis")
        except ZeroDivisionError:
            pass


calculadora = Calculadora()
