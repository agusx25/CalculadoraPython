from tkinter import *
from tkinter import ttk


class Calculadora():
    def __init__(self):
        root = Tk()
        self.LabelResultado = '0'
        self.frm = ttk.Frame(root, padding=10)
        self.frm.grid()
        self.operators = ['+', '-', '*', '/']
        self.ttkLabel = ttk.Label(self.frm, text=self.LabelResultado).grid(column=4, row=0)
        #self.ttkLabel.pack()
        for i in range(1, 10):
            column = i-3 * ((i-1)//3)
            row = (i+2)//3
            ttk.Button(self.frm, text=i, command=lambda i=i :self.add_numbers(str(i))).grid(column=column, row=row)
        for i in range(len(self.operators)):
            ttk.Button(self.frm, text=self.operators[i], command=lambda i=i :self.add_numbers(self.operators[i])).grid(column=4, row=i+1)
        ttk.Button(self.frm, text='=', command= self.solve_equation).grid(column=4, row=4)
        root.mainloop()

    def add_numbers(self, number=0):
        # if self.LabelResultado == '0' and number.isnumeric():
        #     self.ttkLabel.config(text=number)
        #     #ttk.Label(self.frm, text=number).grid(column=4, row=0)
        #     self.LabelResultado = number
        # else:
        #     self.LabelResultado += number
        #     self.ttkLabel.config(text=self.LabelResultado)
        #     #ttk.Label(self.frm, text=self.LabelResultado).grid(column=4, row=0)
        pass
    def solve_equation(self):
        #self.ttkLabel.config(text=self.LabelResultado)
        #ttk.Label(self.frm, text=eval(self.LabelResultado)).grid(column=4, row=0)
        pass



calculadora = Calculadora()
