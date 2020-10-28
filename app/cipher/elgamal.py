import random
from app.util.util import generate_prime, power
'''
key generator
1. pick p (prime number)
2. pick g (g < p)
3. pick x (1 <= x <= p-2)
4. calculate y (g^x mod p)
5. Return public key (y, g, p) and private key (x, p)
'''


def generate_elgamal_keys(size):
    p = generate_prime(size)
    g = random.randint(1, p-1)
    x = random.randint(1, p-2)

    y = power(g, x, p)

    pub_key = (y, g, p)
    pri_key = (x, p)

    return pub_key, pri_key
