""" Solver Linear equation using inverse matrix """
import numpy as np


class LinearEquationSolver(object):

    def __init__(self, A, B):
        self.A = A
        self.B = B

    def is_valid(self):

        shape_A = self.A.shape
        shape_B = self.B.shape

        if shape_A[1] == shape_B[0]:
            if shape_A[0] == shape_A[1]:
                return True
            else:
                raise Exception("A is not a Square matrix")
        else:
            raise Exception("Dot Product not possible for A and B")

    def inverse_matrix(self, matrix):
        """ Inverse the matrix """
        try:
            inverse_matix = np.linalg.inv(matrix)
            return inverse_matix
        except Exception as e:
            raise ValueError(f"Inverse of matrix not possible: {e}")

    # def solve(self):
    #     """Optimized solve method using numpy.linalg.solve."""
    #     if self.is_valid():
    #         return np.linalg.solve(self.A, self.B)
    def solve(self):

        coff = 0
        if self.is_valid():
            inverse_A = self.inverse_matrix(self.A)
            coff = np.dot(inverse_A, self.B)

        return coff
