
import math # only for testing purposes


def ceil(a):
    #returns the smallest integer greater than or equal to a
    #tested with unittest
    if a == int(a):
        return int(a)
    elif a > 0:
        return int(a) + 1
    elif a < 0:
        return int(a)
    else:
        return 0
    
def floor(a): 
    #returns the largest integer less than or equal to a
    #tested with unittest
    if a == int(a):
        return int(a)
    elif a > 0:
        return int(a)
    elif a < 0:
        return int(a) - 1
    else:
        return 0

def sqrt(a, precision=0.000001):
    #returns the square root of a
    #tested with unittest
    #This method is based on the Newton's method
    '''
    Proof:
    Newton's Method: X_n+1 = Xn - f(Xn)/f'(Xn)
    Let f(x) = x^2 - a
    f'(x) = 2x
    X_n+1 = Xn - (Xn^2 - a)/2Xn
    X_n+1 = 1/2 * (Xn + a/Xn)
    '''
    if a <= 0:
        raise ValueError("Input must be a positive number")
    else:
        x = a
        while True:
            root = 0.5 * (x + a/x)
            if abs(root - x) < precision:
                return root
            x = root


def swap(a, b):
    a = a^b
    b = a^b
    a = a^b
    return a, b
    
def fast_reciprocal_sqrt(a):
    #Magic number: 0x5F3759DF
    '''
    Original C code:
    float Q_rsqrt(float number)
        {
        long i;
        float x2, y;
        const float threehalfs = 1.5F;

        x2 = number * 0.5F;
        y  = number;
        i  = * ( long * ) &y;                       // evil floating point bit level hacking
        i  = 0x5f3759df - ( i >> 1 );               // what the fuck?
        y  = * ( float * ) &i;
        y  = y * ( threehalfs - ( x2 * y * y ) );   // 1st iteration
        // y  = y * ( threehalfs - ( x2 * y * y ) );   // 2nd iteration, this can be removed

        return y;
        }
    '''
    
    pass

def fast_pow(a, power, p):
    rtn  = 1
    if power < 0:
        inverse = Extended_Euclidian_Algorithm(a, p)[0]
        if inverse < 0:
            inverse += p
        a = inverse
        power = -power
    if a > p:
        a = a % p
    while power > 0:
        if power % 2 == 1: #odd
            rtn = (rtn * a) % p
        power = power >> 1
        a = (a * a) % p    
    return rtn



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
        
def fermat_isPrime(a):
    #This function uses Fermat's Little Theorem
    #a^(p-1) = 1 mod p
    #This is a probabilistic algorithm
    #This algorithm cannot exclude Carmichael numbers
    if a < 2:
        return False
    if a == 2:
        return True
    else:
        return fast_pow(2,a-1,a) == 1

def factor_out_2(num):
    '''Returns (power of 2, remainer q)'''
    if (not isinstance(num, int)) or (num <= 0):
        raise ValueError("Please input a positive integer.")
    q,r = divmod(num, 2)
    v = 0
    while r == 0:
        v += 1
        num = q
        q, r = divmod(q, 2)
    return (v, num)

def miller_rabin_isPrime(n, a):
    # n = number to be tested
    # a = Miller-Rabin witness
    if n % 2 == 0:
        return "Composite"
    if 1 < gcd(n, a) < n:
        return "Composite"
    
    n_1 = factor_out_2(n-1)
    k = n_1[0]
    q = n_1[1]
    a = pow(a, q, n)
    if a == 1:
        return "Test Fails"
    for i in range(k):
        if a == n-1:
            return "Test Fails"
        a = pow(a, 2, n)
    return "Composite"

def AKS_isPrime(a):
    pass


def _isPrime(a):
    #NEED TESTING
    # This method first check if a is fermat prime
    # if it is then go to miller rabin test to make sure
    fermat_status = fermat_isPrime(a)
    if fermat_status:
        miller_rabin_status = miller_rabin_isPrime(a)
        if miller_rabin_status == "Probably Prime":
            return True
        elif miller_rabin_status == "Composite":
            return False
        else:
            print(" Miller Rabin Test Failed")
            print("Running AKS Test")
            return AKS_isPrime(a)


def genPrime(a):
    #returns a list of prime numbers from 2 to a
    primes = []
    for i in range(2, a+1):
        if isPrime(i):
            primes.append(i)
    return primes

def fast_genPrime(digits):
    '''
    TODO: from 1 to sqrt(a) but also take out the 
    multiples of numbers appeared before might need
     to use a list to store all the numbers
    '''
    pass
        
def gcd(a, b):
    #returns the greatest common divisor of a and b
    #using Euclidean algorithm
    #tested for a, b < 10000
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def naive_facterization(a) -> list:
    #This problem is in NP
    factors = []
    for i in range(2, int(sqrt(a))+1):
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


def isSquare(a):
    if a <= 0:
        raise ValueError("Input must be a positive number")
    return floor(sqrt(a))**2 == a


def fermat_facterization(N) -> list:
    #This method is is based on the representation of an odd integer as the difference of two squares: 
    # a = x^2 - y^2 = (x+y)(x-y)
    if isPrime(N):
        return [N]
    factors = []
    while N % 2 == 0:
        #take out 2 factors first, then we are left with an odd number
        factors.append(2)
        N = N // 2
    if N != 1:
        a = ceil(sqrt(N))
        b2 = a**2 - N
        if b2 == 0:
            factors.append(a)
            factors.append(a)
            return factors
        while b2 > 0 and not isSquare(b2):
            a += 1
            b2 = a**2 - N
        if b2 == 0:
            factors.append(a)
            factors.append(a)
            return factors
        else:
            # Since here we know that b2 is a square number
            b = round(sqrt(b2))
        if isPrime(a+b):
            factors.append(a+b)
        else:
            factors.extend(fermat_facterization(a+b))

        if isPrime(a-b):
            factors.append(a-b)
        else:
            factors.extend(fermat_facterization(a-b))
        if isPrime(a+b) and isPrime(a-b):
            return factors
    else:
        return factors

def pollard_facterization(N) -> list:
    #Suppose that N is a product of two prime numbers
    #N = p*q
    a = 2
    j = 2
    while True:
        a = fast_pow(a, j, N)
        j += 1
        d = gcd(a-1, N)
        if d > 1 and d < N:
            return [d, N//d]

def eular_phi(n):
    phi = 0
    for i in range(1, n):
        if gcd(i, n) == 1:
            phi += 1
    return phi

def euler_mod(a,power, n):
    #Tested with unittest
    #Euler's Phi function
    #first a and n should be coprime
    if gcd(a,n) == 1:
    #first find the a^Phi(n) = 1 mod n
        phi_n = eular_phi(n)
        if power % phi_n == 0:
            return 1
        else:
            return a**(power % phi_n) % n
    else:
        print("a and n are not coprime")


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
        #use a little corallary from Fermat's little theorem
        #that is a^p = a mod p for all a in Z
        if power >= p:
            return littleFermat(p, a, (power%p) + (power//p))
        else:
            return a**power % p
    
def huge_mod(n, a, power):
    #returns a mod n
    if isPrime(n):
        #facterize a
        #a = p1^e1 * p2^e2 * p3^e3 * ... * pk^ek
        """factors = facterize(a)     #this is very costly... need better implementation
        print(factors)
        for i in factors:
            a, power = i"""
            #if n is a prime number
            #we can use Fermat's little theorem
        mod_result = 1
        mod_result *= littleFermat(n, a, power)
        return mod_result % n
    else:
        #if n is not a prime number
        #we can use Euler's theorem
        pass

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


