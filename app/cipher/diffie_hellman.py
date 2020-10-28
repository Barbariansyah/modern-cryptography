import random
from app.util.util import generate_prime, power
'''
key generator
1. pick g and n from params
2. pick x randomly
3. pick y randomly
4. calculate X and Y
5. calculate K
'''


def generate_diffie_keys(n, g, x, y):
    big_x = power(g, x, n)
    big_y = power(g, y, n)

    a_k = power(big_y, x, n) 
    b_k = power(big_x, y, n)

    assert a_k == b_k, "a_k should be the same with b_k"

    return a_k
