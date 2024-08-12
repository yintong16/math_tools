import sys
sys.path.append('C:\\Users\\MAIN\\Desktop\\math_tools')
from modulo import modLib as ml

class FiniteField:

    def __init__(self, p):
        self.p = p

    def add(self, a, b):
        return (a + b) % self.p
    
    def sub(self, a, b):
        return (a - b) % self.p
    
    def mul(self, a, b):
        return (a * b) % self.p
    
    def pow(self, a, power):
        rtn = 1
        if power < 0:
            inverse = ml.Extended_Euclidian_Algorithm(a, self.p)[0]
            if inverse < 0:
                inverse += self.p
            a = inverse
            power = -power
        if a > self.p:
            a = a % self.p
        while power > 0:
            if power % 2 == 1: #odd
                rtn = (rtn * a) % self.p
            power = power >> 1
            a = (a * a) % self.p   
        return rtn
    


