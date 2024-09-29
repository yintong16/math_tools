import random


def get_minor(matrix, row, column):
    #this function returns the minor of a matrix
    minor = []
    for i in range(len(matrix)):
        if i != row:
            minor.append(matrix[i][:column] + matrix[i][column+1:])
    return minor

def det(matrix):
    #this function calculates the determinant of a n x n matrix recursively
    #base case
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    #recursive case
    else:
        determinant = 0
        for i in range(len(matrix)):
            if matrix[0][i] != 0:
                determinant += ((-1)**i) * matrix[0][i] * det(get_minor(matrix, 0, i))
        return determinant

def generate_unimodular_matrix(n):
    #Identity Matrix
    A = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    # Perform random row operations to maintain the determinant ±1
    for _ in range(2 * n):
        # Choose two different rows
        row1, row2 = random.sample(range(n), 2)
        
        # Choose a random integer to multiply row1 by before adding to row2
        factor = random.randint(-5, 5)
        
        # Perform the row operation: row2 = row2 + factor * row1
        for j in range(n):
            A[row2][j] += factor * A[row1][j]
    return A

class GGH:

    def __init__(self, private: list) -> None:
        self.private = private
    
    def generate_public_key(self):
        U = generate_unimodular_matrix(len(self.private))
        det_u = det(U)
        if det_u == 1 or det_u == -1:
            print("det = +-1")
            #W = U*V
            W = U * self.private
            self.public = W
        else:
            raise ValueError("det != +-1")
    
    def babais_algorithm(self, e):
        T = [f"x{i}" for i in range(len(self.private))]
        print(T)