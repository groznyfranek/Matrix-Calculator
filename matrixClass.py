class Matrix:
    def __init__(self, mat):
        self.n = len(mat)
        self.m = len(mat[0])
        self.matrix = [list(row) for row in mat]
