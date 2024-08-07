
def get_dimensions():
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))
    if rows != columns:
        print("The matrix must be square")
        exit()
    return rows

def construct_matrix(file):
    with open(file, "r") as file:
        matrix = []
        row = file.readline().split()
        size = len(row)
        row = list(map(int, row))
        matrix.append(row)
        for i in range(size-1):
            row = file.readline().split()
            row = list(map(int, row))
            matrix.append(row)
    return matrix

def get_minor(matrix, row, column):
    #this function returns the minor of a matrix
    minor = []
    for i in range(len(matrix)):
        if i != row:
            minor.append(matrix[i][:column] + matrix[i][column+1:])
    return minor

#def fast_det(matrix):




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


if __name__ == "__main__":
    matrix = construct_matrix("matrix_input.txt")
    determinant = det(matrix)
    print(f"The determinant of the matrix is: {determinant}")
