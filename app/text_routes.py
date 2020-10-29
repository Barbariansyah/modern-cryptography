from app import app
from flask import request
from .util.create_response import create_cipher_text_response, create_plain_text_response
from .cipher.elgamal import encrypt_elgamal, decrypt_elgamal
from .cipher.rsa import *
import time


@app.route('/')
def index():
    return "Hello, text!"


''' Text encryption '''


@app.route('/encrypt/text/rsa', methods=['POST'])
def encrypt_text_rsa():
    json_request = request.get_json()
    message = json_request['message']
    public_key = json_request['public_key']
    message = bytes(message, encoding='UTF-8')

    start_time = time.time()
    encrypted_message = encrypt_rsa(message, public_key)
    time_needed = time.time() - start_time

    response = create_cipher_text_response(encrypted_message, time_needed)
    return response


@app.route('/encrypt/text/elgamal', methods=['POST'])
def encrypt_text_elgamal():
    json_request = request.get_json()
    message = json_request['message']
    public_key = json_request['public_key']

    message = bytes(message, 'utf-8')

    start_time = time.time()
    encrypted_message = encrypt_elgamal(message, public_key)
    time_needed = time.time() - start_time

    response = create_cipher_text_response(encrypted_message, time_needed)
    return response


''' Text decryption '''


@app.route('/decrypt/text/rsa', methods=['POST'])
def decrypt_text_rsa():
    json_request = request.get_json()
    message = json_request['message']
    private_key = json_request['private_key']
    message = bytes(message, encoding='UTF-8')

    start_time = time.time()
    decrypted_message = decrypt_rsa(message, private_key)
    time_needed = time.time() - start_time

    response = create_plain_text_response(decrypted_message, time_needed)
    return response


@app.route('/decrypt/text/elgamal', methods=['POST'])
def decrypt_text_elgamal():
    json_request = request.get_json()
    message = json_request['message']
    private_key = json_request['private_key']

    message = bytes(message, 'utf-8')

    start_time = time.time()
    decrypted_message = decrypt_elgamal(message, private_key)
    time_needed = time.time() - start_time

    response = create_plain_text_response(decrypted_message, time_needed)
    return response
