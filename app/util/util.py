'''
Greatest Common Divisor
'''
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

'''
Prime Number Checker
'''
def is_prime(a):
    if a > 1:
        for i in range(3, a, 2):
            if a % i == 0:
                return False
        return True
    elif a == 2:
        return True
    else:
        return False

'''
Multiplicative Inverse
'''
def multiplicative_inverse(e, phi) : 
    e = e % phi; 
    for x in range(1, phi) : 
        if ((e * x) % phi == 1) : 
            return x 
    return 1