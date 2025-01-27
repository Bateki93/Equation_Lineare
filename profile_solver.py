import cProfile
from solver import LinearEquationSolver
import numpy as np


def main():
    # Cas de test pour le profilage
    A = np.array([[3, 8], [4, 11]])
    B = np.array([5, 7])
    solver = LinearEquationSolver(A, B)
    solver.solve()
    print(A)


if __name__ == "__main__":
    cProfile.run('main()', 'profiling_output')
