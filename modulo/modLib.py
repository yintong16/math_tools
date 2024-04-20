
import math

def isPrime(a):
    #returns True if a is a prime number, False otherwise
    #tested for a < 1000000
    if a < 2:
        return False
    if a == 2:
        #2 is the only even prime number
        return True
    elif a % 2 == 0:
        #all prime numebers are odd except 2
        return False
    elif a == 3:
        return True
    else:
        #every prime number is in the form of 6k+1 or 6k-1 except 2 and 3
        if (a-1)%6 == 0 or (a+1)%6 == 0:
            #if a is not a prime number, it will have a factor less than or equal to its square root
            for i in range(3, int(a**0.5)+1):
                if a % i == 0:
                    return False
            return True
        else:
            return False
        
def gcd(a, b):
    #returns the greatest common divisor of a and b
    #using Euclidean algorithm
    #tested for a, b < 10000
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def facterize(a):
    #returns a list of tuples of the prime factors of a and their powers
    #tested for a < 1000000
    factors = []
    for i in range(2, int(a**0.5)+1):
        if isPrime(i):
            power = 0
            while a % i == 0:
                a = a // i
                power += 1
            if power > 0:
                factors.append((i, power))
    if a > 1:
        factors.append((a, 1))
    return factors


def euler():
    pass


def littleFermat(p, a, power):
    #here we assume that p is a prime number
    #should be handled in the mod() function
    if gcd(p, a) == 1:
        #if a is coprime to p
        #use Fermat's little theorem
        if power == 0:
            return 1
        elif power == p-1:
            return 1
        elif power > p-1:
            return littleFermat(p, a, power % (p-1))
        else:
            return a**power % p
    else:
        #if a is not coprime to p
        #use the second part of Fermat's little theorem
        #that is a^p = a mod p
        if power >= p:
            return littleFermat(p, a, (power%p) + (power//p))
        else:
            return a**power % p
            
            
    
def mod(a, n):
    #facterize a
    #a = p1^e1 * p2^e2 * p3^e3 * ... * pk^ek
    facterize(a)



    if isPrime(n):
        #if n is a prime number
        #we can use Fermat's little theorem
        littleFermat(n, a, power)

