from app.util.util import *
from app.cipher.rsa import *
from Crypto.Util import number
from pathlib import Path

resource_path = Path('./app')

if __name__ == "__main__":
    '''
    prime test
    '''
    # print(is_prime(15))
    '''
    multiplicative inverse
    '''
    # print(extended_euclidian(7, 40))
    '''
    prime generator
    '''
    # print(generate_prime(48))
    # print(generate_prime(48))
    # print(generate_prime(48))
    # print(number.getPrime(128))
    # print(number.getPrime(128))
    '''
    key generation
    '''
    # print(generate_rsa_keys(128))
    n, d, e = generate_rsa_keys(128)
    print(n)
    print(d)
    print(e)
    file_name = resource_path/'file_resources/sample_text.txt'
    content = None
    with open(file_name, 'rb') as f:
        content = f.read()
    # print(type(content))
    # for b in content:
    #     print(b, end=', ')
    print('start encryption')
    encrypted_bytes = encrypt_rsa(content, n, e)
    # modified_content = []
    # for b in content:
    #     modified_content.append(b)
    # for b in modified_content:
    #     print(b, end=', ')
    # modified_content_bytes = bytes(modified_content)
    # print(modified_content_bytes)
    # print(content)
    # content = bytes_to_bits(content)
    # print(len(content))
