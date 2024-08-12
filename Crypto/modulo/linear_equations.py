#Solving linear equations in Finite Fields
#Given a linear equation ax = b in a finite field Fp, we want to find the value of x.
#We can use the Extended Euclidean Algorithm to solve this equation.

def Euclidian_Algorithm(a, b):
    if b == 0:
        return a
    else:
        return Euclidian_Algorithm(b, a % b)

def Extended_Euclidian_Algorithm(a, b):
    if b == 0:
        return (1, 0)
    else:
        (x, y) = Extended_Euclidian_Algorithm(b, a % b)
        return (y, x - (a // b) * y)



if __name__ == "__main__":
    #input
    a,b,p = map(int, input().split())
    #if a is not coprime to p
    if Euclidian_Algorithm(a, p) != 1:
        print("The equation has no solution")
    else:
        #find the multiplicative inverse of a
        inv = Extended_Euclidian_Algorithm(a, p)[0] % p
        #find the solution
        x = (inv * b) % p
        print(x)