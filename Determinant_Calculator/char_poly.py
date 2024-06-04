import numpy as np


def read_matrix(file):
    with open(file, "r") as file:
        matrix = []
        for line in file:
            row = list(map(int, line.split()))
            matrix.append(row)
    return matrix


def char_poly(matrix):
    # matrix = np.matrix(matrix)
    return np.poly(matrix)


matrix = read_matrix("matrix_input.txt")
poly = char_poly(matrix)
print(f"The characteristic polynomial of the matrix is: {poly}")