import sys
sys.path.append('C:\\Users\\MAIN\\Desktop\\math_tools\\Crypto')
from modulo import modLib as ml

def gaussian_elimination(A, b):
    n = len(A)
    
    # Augment A with b
    for i in range(n):
        A[i].append(b[i])

    # Forward elimination process
    for i in range(n):
        # Find the pivot row and swap it with the current row
        max_row = i + max(range(n - i), key=lambda k: abs(A[i + k][i]))
        A[i], A[max_row] = A[max_row], A[i]

        # Make the pivot element equal to 1
        pivot = A[i][i]
        for j in range(i, n + 1):
            A[i][j] /= pivot
        
        # Eliminate the current variable from the subsequent rows
        for k in range(i + 1, n):
            factor = A[k][i]
            for j in range(i, n + 1):
                A[k][j] -= factor * A[i][j]

    # Back substitution process
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = A[i][n] - sum(A[i][j] * x[j] for j in range(i + 1, n))
    
    return x


def norm(v:list):
        return ml.sqrt(sum([i**2 for i in v]))
    


def gaussian_reduction(v1:list, v2:list):
    # Let the lattice L be a 2-dimensional lattice with basis v1, and v2. 
    # This algorithm gives a good basis for the given basis. 
    while True:
        v1_norm = norm(v1)
        v2_norm = norm(v2)
        if v2_norm < v1_norm:
            temp = v1
            v1 = v2
            v2 = temp
            # now ||v2|| >= ||v1||
            v1_norm_sq = (norm(v1))**2
            v1v2 = sum([v1[i]*v2[i] for i in range(len(v1))])
            m = round(v1v2/v1_norm_sq)
            if m == 0:
                return v1, v2
            v2_new = []
            for i in range(len(v1)):
                v2_new.append(v2[i]-m*v1[i])
            v2 = v2_new
            print("v1=", v1, "v2=", v2, "m=", m)

