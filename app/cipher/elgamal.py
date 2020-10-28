import random
from app.util.util import generate_prime, power, hex_to_decimal, decimal_to_hex
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


def encrypt_elgamal(plaintext, key):
    ciphertext = []
    key = key.split('\n')
    y = hex_to_decimal(key[1])
    g = hex_to_decimal(key[2])
    p = hex_to_decimal(key[3])

    k = random.randint(1, p-1)

    for i in range(len(plaintext)):
        a = power(g, k, p)
        y_k = power(y, k, p)
        m_k = plaintext[i] % p
        b = (y_k * m_k) % p

        a = decimal_to_hex(a)
        b = decimal_to_hex(b)

        ciphertext.append(a)
        ciphertext.append(b)

    ciphertext = " ".join(ciphertext)
    return ciphertext


def decrypt_elgamal(ciphertext, key):
    plaintext = []
    key = key.split('\n')
    x = hex_to_decimal(key[1])
    p = hex_to_decimal(key[2])
    ciphertext = ciphertext.split(' ')

    for i in range(0, len(ciphertext), 2):
        a = hex_to_decimal(ciphertext[i])
        b = hex_to_decimal(ciphertext[i+1])
        ax_inverse = power(a, p-1-x, p)
        m = b * ax_inverse % p
        plaintext.append(m)

    plaintext = bytes(plaintext)
    return plaintext
