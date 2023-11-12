from matrixClass import Matrix
import numpy as np


class Multiplier:
    def __init__(self):
        pass

    def multiply(A: Matrix, B: Matrix):
        if (len(A.matrix[0]) != len(B.matrix)):
            return 'Wrong inputs'
        output = np.array(A.matrix) @ np.array(B.matrix)
        return Matrix(output.tolist())

    def transpoze(A: Matrix):
        output = np.transpose(A.matrix)
        return Matrix(output.tolist())

    def inverse(A: Matrix):
        output = np.linalg.inv(A.matrix)
        return Matrix(output.tolist())
