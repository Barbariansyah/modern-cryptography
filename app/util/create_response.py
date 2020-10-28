import os
import time

save_path = os.getcwd() + '/app/file_resources/'
full_path = os.path.abspath(os.path.join(os.path.realpath(__file__), '../..'))


def create_plain_text_response(plaintext):
    if (type(plaintext) == bytes):
        plaintext = "".join([chr(i) for i in plaintext])
    return ({'plaintext': plaintext})


def create_cipher_text_response(cipher_text):
    n = 5
    if (type(cipher_text) == bytes):
        cipher_text = "".join([chr(i) for i in cipher_text])
    return ({'ciphertext': cipher_text})


def create_file_response(filename, cipher_text):
    filename = str(int(time.time())) + '.encrypted.' + filename
    complete_filename = os.path.join(full_path, 'file_resources', filename)
    if type(cipher_text) == str:
        cipher_text = cipher_text.encode()
    with open(complete_filename, 'wb+') as f:
        f.write(cipher_text)

    return complete_filename


def create_key_response(pub_key, pri_key):
    pub_key = '-----BEGIN PUBLIC KEY----- \n ' + \
        pub_key + '-----END PUBLIC KEY----- \n'
    pri_key = '-----BEGIN RSA PRIVATE KEY----- \n ' + \
        pri_key + '-----END RSA PRIVATE KEY----- \n'

    return ({'public_key': pub_key, 'private_key': pri_key})


def create_diffie_response(key):
    return ({'secret_key': key})
