from app import app
from flask import request


@app.route('/key')
def index_key():
    return "Hello, key!"


''' Key generation '''


@app.route('/key/diffie', methods=['POST'])
def generate_diffie_key():
    pass


@app.route('/key/rsa', methods=['POST'])
def generate_rsa_key():
    pass


@app.route('/key/elgamal', methods=['POST'])
def generate_elgamal_key():
    pass
