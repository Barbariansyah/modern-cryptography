from app.util.util import *
from app.cipher.elgamal import *

if __name__ == "__main__":
    print(generate_elgamal_keys(48))

    a = 1430
    b = 697
    x = 1751
    p = 2357

    ax_inverse = power(a, p-1-x, p)
    m = b * ax_inverse % p
    print(m)
    # print(encrypt_elgamal(bytes("dika", encoding='utf-8'), "-----BEGIN PUBLIC KEY----- \n 157ca0851b0 \n f3bf2a467303 \n 100000000022b \n -----END PUBLIC KEY----- \n"))