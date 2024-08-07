import matplotlib.pyplot as plt
import numpy as np
from fractions import Fraction



class EllipticCurve:

    INF = (float('inf'), float('inf'))

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
            else:
                slope = (y2 - y1) / (x2 - x1)
            x3 = slope**2 - x1 - x2
            y3 = slope*(x1 - x3) - y1
            if faction:
                x3 = Fraction(x3).limit_denominator()
                y3 = Fraction(y3).limit_denominator()
            return(x3, y3)
        

        