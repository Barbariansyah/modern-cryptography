import math

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
def multiplicative_inverse(e, totient) : 
    e = e % totient; 
    for x in range(1, totient) : 
        if ((e * x) % totient == 1) : 
            return x 
    return 1

'''
generate prime up to 48 bit
in: size in bit, random seed
'''
def generate_prime(size, seed):
    start_binary = '1' + '0' * (size - 1)
    prime = binary_to_int(start_binary)
    
    if prime % 2 == 0:
        prime += 1

    while not is_prime(prime):
        prime += 2
    
    return prime