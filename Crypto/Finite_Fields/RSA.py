import sys
sys.path.append('C:\\Users\\MAIN\\Desktop\\math_tools\\Crypto')
from modulo import modLib as ml




####################### RSA EXPLOITS ####################
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


def factor_with_private_key(n, a, e1, d1):
    if n % 2 == 0:
        return "Composite"
    if 1 < ml.gcd(n, a) < n:
        return "Composite"
    
    n_1 = factor_out_2(e1 * d1 - 1)
    k = n_1[0]
    q = n_1[1]
    a = ml.fast_pow(a, q, n)
    if a == 1:
        return "Test Fails"
    for i in range(k):
        if a == n-1:
            return "Test Fails"
        a = ml.fast_pow(a, 2, n)
    return "Composite"
