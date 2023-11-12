import tkinter as tk
import numpy as np
from matrixClass import Matrix
from multiplierClass import Multiplier
from tkinter import messagebox


class Calculator:
    def __init__(self, dimension, title):
        self.root = tk.Tk()  # window
        self.root.geometry(dimension)
        self.root.title(title)

        # list of user's inputs
        self.A = Matrix([['' for _ in range(3)] for _ in range(3)])
        self.B = Matrix([['' for _ in range(3)] for _ in range(3)])
        self.C = Matrix([['' for _ in range(3)] for _ in range(3)])
        self.multiplier = Multiplier

        self.input_A = [[tk.Entry(self.root, width=5) for _ in range(3)] for _ in range(3)]
        self.input_B = [[tk.Entry(self.root, width=5) for _ in range(3)] for _ in range(3)]
        self.output_C = [[tk.Label(self.root, text='-', width=5) for _ in range(3)] for _ in range(3)]

        # render
        separator_column = 3
        for i in range(3):
            tk.Label(self.root, text=" ").grid(row=0, column=separator_column + i)
        for i in range(3):
            for j in range(3):
                self.input_A[i][j].grid(row=i + 5, column=j, padx=10, pady=10)
                self.input_B[i][j].grid(row=i + 5, column=j + 6, padx=10, pady=10)
                self.output_C[i][j].grid(row=i + 5, column=j + 12, padx=10, pady=10)

        # labels
        self.A_Label = tk.Label(self.root, text='A').grid(row=8, column=1)
        self.B_Label = tk.Label(self.root, text='B').grid(row=8, column=7)
        self.output_Label = tk.Label(self.root, text='output').grid(row=8, column=13)

        # buttons
        tk.Label(self.root, text='').grid(row=10, column=0)
        self.AxB = tk.Button(self.root, text='AxB', command=self.calculate_AxB).grid(row=11, column=0)
        self.A_transpoze = tk.Button(self.root, text='AT', command=self.A_transpoze).grid(row=11, column=1)
        self.A_inv = tk.Button(self.root, text='A^-1', command=self.calculate_A_inv).grid(row=11, column=2)

    def load_inputs(self, check_B):
        for i in range(self.A.n):
            for j in range(self.A.m):
                try:
                    self.A.matrix[i][j] = int(self.input_A[i][j].get())
                except ValueError:
                    messagebox.showerror("Error", "Wrong inputs!")
                    self.clear_all()
                    return False

        if check_B:
            for i in range(self.B.n):
                for j in range(self.B.m):
                    try:
                        self.B.matrix[i][j] = int(self.input_B[i][j].get())
                    except ValueError:
                        messagebox.showerror("Error", "Wrong inputs!")
                        self.clear_all()
                        return False

    def calculate_AxB(self):
        self.load_inputs(check_B=True)
        self.C = self.multiplier.multiply(self.A, self.B)
        self.print_output()

    def print_output(self):
        for i in range(3):
            for j in range(3):
                self.output_C[i][j].config(text=str(self.C.matrix[i][j]))

    def check_matrix(self, X: Matrix):
        # to do, to unable multiplying non - square matrices
        pass

    def A_transpoze(self):
        self.load_inputs(check_B=False)
        self.C = self.multiplier.transpoze(self.A)
        self.print_output()

    def calculate_A_inv(self):
        self.load_inputs(check_B=False)
        if np.linalg.det(self.A.matrix) == 0:
            messagebox.showerror("Error", "Wrong inputs!")
            self.clear_all()
            return False
        self.C = self.multiplier.inverse(self.A)
        self.print_output()

    def clear_all(self):
        self.A = Matrix([['' for _ in range(3)] for _ in range(3)])
        self.B = Matrix([['' for _ in range(3)] for _ in range(3)])
        self.C = Matrix([['' for _ in range(3)] for _ in range(3)])

    def run(self):
        self.root.mainloop()
