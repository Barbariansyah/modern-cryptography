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
    splitted_ciphertext = [cipher_text[i:i+n]
                           for i in range(0, len(cipher_text), n)]
    return ({'ciphertext': cipher_text, 'splitted_ciphertext': splitted_ciphertext})


def create_file_response(filename, cipher_text):
    filename = str(int(time.time())) + '.encrypted.' + filename
    complete_filename = os.path.join(full_path, 'file_resources', filename)
    if type(cipher_text) == str:
        cipher_text = cipher_text.encode()
    with open(complete_filename, 'wb+') as f:
        f.write(cipher_text)

    return complete_filename
