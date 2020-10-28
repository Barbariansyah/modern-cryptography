from app import app
from flask import request
from .util.create_response import create_cipher_text_response, create_plain_text_response
from .cipher.elgamal import encrypt_elgamal, decrypt_elgamal


@app.route('/')
def index():
    return "Hello, text!"


''' Text encryption '''


@app.route('/encrypt/text/rsa', methods=['POST'])
def encrypt_text_rsa():
    json_request = request.get_json()
    query = json_request['message']
    key = json_request['key']
    encrypted_text = query  # TODO

    response = create_cipher_text_response(encrypted_text)
    return response


@app.route('/encrypt/text/elgamal', methods=['POST'])
def encrypt_text_elgamal():
    json_request = request.get_json()
    query = json_request['message']
    key = json_request['key']

    query = bytes(query, 'utf-8')

    encrypted_text = encrypt_elgamal(query, key)

    response = create_cipher_text_response(encrypted_text)
    return response


''' Text decryption '''


@app.route('/decrypt/text/rsa', methods=['POST'])
def decrypt_text_rsa():
    json_request = request.get_json()
    query = json_request['message']
    key = json_request['key']
    decrypted_text = query  # TODO

    response = create_plain_text_response(decrypted_text)
    return response


@app.route('/decrypt/text/elgamal', methods=['POST'])
def decrypt_text_elgamal():
    json_request = request.get_json()
    query = json_request['message']
    key = json_request['key']
    decrypted_text = decrypt_elgamal(query, key)

    response = create_plain_text_response(decrypted_text)
    return response
