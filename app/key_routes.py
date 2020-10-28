from app import app
from flask import request
from app.cipher.diffie_hellman import generate_diffie_keys
from app.cipher.elgamal import generate_elgamal_keys
from app.cipher.rsa import generate_keys
from app.util.util import decimal_to_hex
from app.util.create_response import create_key_response, create_diffie_response


@app.route('/key')
def index_key():
    return "Hello, key!"


''' Key generation '''


@app.route('/key/diffie', methods=['POST'])
def generate_diffie_key():
    json_request = request.get_json()
    n = json_request['n']
    g = json_request['g']
    x = json_request['x']
    y = json_request['y']
    key = generate_diffie_keys(n, g, x, y)

    response = create_diffie_response(key) 
    return response


@app.route('/key/rsa', methods=['GET'])
def generate_rsa_key():
    n, d, e = generate_keys(48)
    pub_key = (e, n)
    pri_key = (d, n)

    pub_key = [(decimal_to_hex(i) + ' \n ') for i in pub_key]
    pub_key = ''.join(pub_key)

    pri_key = [(decimal_to_hex(i) + ' \n ') for i in pri_key]
    pri_key = ''.join(pri_key)

    response = create_key_response(pub_key, pri_key)
    return response


@app.route('/key/elgamal', methods=['GET'])
def generate_elgamal_key():
    pub_key, pri_key = generate_elgamal_keys(48)
    pub_key = [(decimal_to_hex(i) + ' \n ') for i in pub_key]
    pub_key = ''.join(pub_key)

    pri_key = [(decimal_to_hex(i) + ' \n ') for i in pri_key]
    pri_key = ''.join(pri_key)

    response = create_key_response(pub_key, pri_key)
    return response
