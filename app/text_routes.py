from app import app
from flask import request


@app.route('/')
def index():
    return "Hello, text!"


''' Text encryption '''


@app.route('/encrypt/text/rsa', methods=['POST'])
def encrypt_text_rsa():
    pass


@app.route('/encrypt/text/elgamal', methods=['POST'])
def encrypt_text_elgamal():
    pass


''' Text decryption '''


@app.route('/decrypt/text/rsa', methods=['POST'])
def decrypt_text_rsa():
    pass


@app.route('/decrypt/text/elgamal', methods=['POST'])
def decrypt_text_elgamal():
    pass
