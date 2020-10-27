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
        for i in range(2, a):
            if a % i == 0:
                return False
        return True
    else:
        return False