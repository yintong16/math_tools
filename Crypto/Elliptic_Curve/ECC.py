import matplotlib.pyplot as plt
import numpy as np
from fractions import Fraction
import sys
sys.path.append('C:\\Users\\YintongLuo\\Desktop\\math_tools\\Crypto')
from modulo import modLib as ml


class EllipticCurve:

    INF = (float('inf'), float('inf'))

    #simply version of elliptic curve
    def __init__(self, A, B):
        self.A = A
        self.B = B
    
    
    def plot_elliptic_curve(self):
        x = np.linspace(-10, 10, 400)
        y = np.linspace(-10, 10, 400)
        X, Y = np.meshgrid(x, y)
        F = X**3 + self.A*X + self.B - Y**2
        plt.contour(X, Y, F, [0], colors='r')
        plt.grid()
        plt.show()


    def add(self, P: tuple, Q: tuple, faction=False):
        if P == self.INF:
            return Q
        if Q == self.INF:
            return P
        x1, y1 = P
        x2, y2 = Q
        # check if P and Q are points on the curve
        if y1**2 != x1**3 + self.A*x1 + self.B:
            raise ValueError(f"{P} is not on the curve")
        if y2**2 != x2**3 + self.A*x2 + self.B:
            raise ValueError(f"{Q} is not on the curve")
        
        if x1 == x2 and y1 == -y2:
            return self.INF
        else:
            if P == Q:
                slope = (3*x1**2 + self.A) / (2*y1) #Tangent line
                print("Lambda = ", slope)
            else:
                slope = (y2 - y1) / (x2 - x1)
            x3 = slope**2 - x1 - x2
            y3 = slope*(x1 - x3) - y1
            print(slope, x1, x2)
            if faction:
                x3 = Fraction(x3).limit_denominator()
                y3 = Fraction(y3).limit_denominator()
            return(x3, y3)
    
    
    def count_integer_coordinates(self, x_range: int, y_range: int):
        count = 0
        for x in range(x_range):
            for y in range(y_range):
                y2 = x**3 + self.A*x + self.B
                if ml.isSquare(y2):
                    y = int(ml.sqrt(y2))
                    count += 1 if y == 0 else 2
        return count
        
    
class EllipticCurveFiniteField:

    INF = (float('inf'), float('inf'))

    def __init__(self, A, B, p):
        self.A = A
        self.B = B
        self.p = p #modulus
        
    def add(self, P: tuple, Q: tuple):
        if P == self.INF:
            return Q
        if Q == self.INF:
            return P
        x1, y1 = P
        x2, y2 = Q
        # check if P and Q are points on the curve
        if ((y1**2) % self.p) != (x1**3 + self.A*x1 + self.B) % self.p:
            raise ValueError(f"{P} is not on the curve")
        if ((y2**2) % self.p) != (x2**3 + self.A*x2 + self.B) % self.p:
            raise ValueError(f"{Q} is not on the curve")
        
        if x1 == x2 and y1 == -y2:
            return self.INF
        else:
            if P == Q:
                numerator = (3*x1**2 + self.A) % self.p
                denominator = (2*y1) % self.p
                if ml.gcd(denominator, self.p) > 1:
                    print("gcd > 1 when denominator = ", denominator)
                    raise ValueError
                inverse = ml.Extended_Euclidian_Algorithm(denominator, self.p)[0]
                slope = (numerator * inverse) % self.p
                # print("Lambda = ", slope)
            else:
                numerator = (y2 - y1) % self.p
                denominator = (x2 - x1) % self.p
                if ml.gcd(denominator, self.p) > 1:
                    print("gcd > 1 when denominator = ", denominator)
                    raise ValueError
                inverse = ml.Extended_Euclidian_Algorithm(denominator, self.p)[0]
                slope = (numerator * inverse) % self.p
                # print("Lambda = ", slope)
            x3 = (slope**2 - x1 - x2) % self.p
            y3 = (slope*(x1 - x3) - y1) % self.p
            return(x3, y3)
        
    def pow(self, P: tuple, power):
        if power < 0:
            inverse = -P[1] # inverse of (x, y) = (x, -y)
            while inverse < 0:
                inverse += self.p
            P = (P[0], inverse)
            power = -power
        Q = P
        R = self.INF
        while power > 0:
            if power % 2 == 1: #odd
                R = self.add(R, Q)
            Q = self.add(Q, Q)
            power = power >> 1
        return R


def EC_Lenstra_fatorization(N, A, B, P: tuple):
    # N is the numeber to be factored 
    ec = EllipticCurveFiniteField(A, B, N)
    try:
        i = 1
        nP = P
        while True:
            i += 1
            nP = ec.pow(nP, i)
            print(f"{i}!P = {nP}")
    except ValueError:
        print("Failed at: ", i, "!")
        

class WeierstrassEllipticCurve:
    INF = (float('inf'), float('inf'))

    #simply version of elliptic curve
    def __init__(self, a1, a2, a3, a4, a6):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.a4 = a4
        self.a6 = a6

    
    
    def plot_elliptic_curve(self):
        x = np.linspace(-10, 10, 400)
        y = np.linspace(-10, 10, 400)
        X, Y = np.meshgrid(x, y)
        F = Y**2 + self.a1*X*Y + self.a3*Y - X**3 - self.a2*X**2 - self.a4*X - self.a6
        plt.contour(X, Y, F, [0], colors='r')
        plt.grid()
        plt.show()


    def add(self, P: tuple, Q: tuple, faction=False):
        pass