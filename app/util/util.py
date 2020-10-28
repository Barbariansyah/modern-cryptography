import math
import random

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
def is_prime(n):
    if n % 2 == 0 or n <= 1:
        return False
    elif n == 2:
        return True
    else:
        sqr = int(math.sqrt(n)) + 1

        for i in range(3, sqr, 2):
            if n % i == 0:
                return False
        return True


'''
binary to int
'''
def binary_to_int(binary):
    return int(binary, 2)


'''
Multiplicative Inverse
'''
def multiplicative_inverse(a, b):
    if a <= b:
        return ValueError('not a > b')
    x0, x1, y0, y1 = 1, 0, 0, 1
    while a != 0:
        q, b, a = b // a, a, b % a
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return b, y0, x0


'''
generate prime up to 48 bit
in: size in bit, random seed
'''
def generate_prime(size):
    change = random.randint(1, size-1)
    start_binary = '1' + '0' * (size - 1)
    start_binary = start_binary[:change] + '1' + start_binary[change:]
    prime = binary_to_int(start_binary)

    if prime % 2 == 0:
        prime += 1

    while not is_prime(prime):
        prime += 2

    return prime


'''
decimal to hexadecimal string
'''
def decimal_to_hex(d):
    return hex(d)[2:]


'''
hexadeximal string to decimal
'''
def hex_to_decimal(h):
    return int(h, 16)


'''
modular exponentiation, taken from https://github.com/csknk/fast-modular-exponentiation
'''
def power(b, e, m):
    r = 1
    if 1 & e:
        r = b
    while e:
        e >>= 1
        b = (b * b) % m
        if e & 1: r = (r * b) % m
    return r
