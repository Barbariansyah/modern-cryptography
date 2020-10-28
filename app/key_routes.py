from app import app
from flask import request
from app.cipher.diffie_hellman import generate_diffie_keys
from app.cipher.elgamal import generate_elgamal_keys
from app.cipher.rsa import generate_rsa_keys
from app.util.util import decimal_to_hex
from app.util.create_response import create_key_response, create_diffie_response
import time


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

    start_time = time.time()
    key = generate_diffie_keys(n, g, x, y)
    time_needed = time.time() - start_time

    response = create_diffie_response(key, time_needed)
    return response


@app.route('/key/rsa', methods=['GET'])
def generate_rsa_key():
    start_time = time.time()
    n, d, e = generate_rsa_keys(128)
    time_needed = time.time() - start_time

    pub_key = (e, n)
    pri_key = (d, n)

    pub_key = [(decimal_to_hex(i) + ' \n ') for i in pub_key]
    pub_key = ''.join(pub_key)

    pri_key = [(decimal_to_hex(i) + ' \n ') for i in pri_key]
    pri_key = ''.join(pri_key)

    response = create_key_response(pub_key, pri_key, time_needed)
    return response


@app.route('/key/elgamal', methods=['GET'])
def generate_elgamal_key():
    start_time = time.time()
    pub_key, pri_key = generate_elgamal_keys(128)
    time_needed = time.time() - start_time

    pub_key = [(decimal_to_hex(i) + ' \n ') for i in pub_key]
    pub_key = ''.join(pub_key)

    pri_key = [(decimal_to_hex(i) + ' \n ') for i in pri_key]
    pri_key = ''.join(pri_key)

    response = create_key_response(pub_key, pri_key, time_needed)
    return response
