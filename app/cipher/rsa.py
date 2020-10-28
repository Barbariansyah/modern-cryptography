import random
import math
from app.util.util import *
from Crypto.Util import number
'''
key generator
1. pick p and q (prime number)
2. calculate toitent func
3. pick e and d
'''

def generate_rsa_keys(size):
    p = number.getPrime(size)
    q = number.getPrime(size)
    n = p * q

    phi = (p - 1) * (q - 1)

    while True:
        e = random.randint(2, phi - 1)
        if gcd(e, phi) == 1:
            gcd_res, s, t = extended_euclidian(phi, e)
            if gcd_res == (s * phi + t * e):
                d = t % phi
                break

    return (n, d, e)

def encrypt_rsa(plain_bytes, public_key):
    key = public_key.split('\n')
    e = hex_to_decimal(key[1])
    n = hex_to_decimal(key[2])
    encrypted_content = []
    decimals = []
    for b in plain_bytes:
        temp = pow(b, e, n)
        decimals.append(temp)
        encrypted_content.append(decimal_to_hex(temp))
    encrypted_content = " ".join(x for x in encrypted_content)
    return encrypted_content      

def decrypt_rsa(cipher_bytes, private_key):
    key = private_key.split('\n')
    d = hex_to_decimal(key[1])
    n = hex_to_decimal(key[2])
    cipher_srting = cipher_bytes.decode()
    cipher_list = cipher_srting.split(' ')
    decrypted_content = []
    for c in cipher_list:
        c_integer = hex_to_decimal(c)
        decrypted_content.append(pow(c_integer, d, n))
    decrypted_content_bytes = bytes(decrypted_content)
    return decrypted_content_bytes 