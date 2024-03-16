
def get_dimensions():
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))
    if rows != columns:
        print("The matrix must be square")
        exit()
    return rows

def construct_matrix(size):
    matrix = []
    for i in range(size):
        raw = input(f"Enter the values for row {i+1} separated by a space: ")
        print(raw)
        row  = raw.split()
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
            determinant += ((-1)**i) * matrix[0][i] * det(get_minor(matrix, 0, i))
        return determinant


if __name__ == "__main__":
    size = get_dimensions()
    matrix = construct_matrix(size)
    determinant = det(matrix)
    print(f"The determinant of the matrix is: {determinant}")
