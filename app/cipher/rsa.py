import random
from app.util.util import *
'''
key generator
1. pick p and q (prime number)
2. calculate toitent func
3. pick e and d
'''

def generate_keys(size):
    p = generate_prime(size)
    q = generate_prime(size)
    n = p * q

    phi = (p - 1) * (q - 1)

    while True:
        e = random.randint(2, phi - 1)
        if gcd(e, phi) == 1:
            gcd_res, s, t = multiplicative_inverse(phi, e)
            if gcd_res == (s * phi + t * e):
                d = t % phi
                break

    return (n, d, e)


