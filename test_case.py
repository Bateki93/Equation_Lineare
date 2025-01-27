
import unittest
import numpy as np

from solver import LinearEquationSolver


class LinearEquationSolverTest(unittest.TestCase):
    def test_one(self):
        A = np.array([[3, 8], [4, 11]])
        B = np.array([5, 7])
        solver = LinearEquationSolver(A, B)
        coff = solver.solve()
        self.assertTrue(np.array_equal(coff, [-1., 1.]))

    def test_two(self):
        A = np.array([[2, 3], [5, 7]])
        B = np.array([8, 19])
        solver = LinearEquationSolver(A, B)
        coff = solver.solve()
        self.assertTrue(np.array_equal(coff, [1., 2.]))


if __name__ == "__main__":
    unittest.main()
