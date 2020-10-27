from app import app
from flask import request, send_file, jsonify


@app.route('/file')
def index_file():
    return "Hello, file!"


''' File encryption '''


@app.route('/encrypt/file/rsa', methods=['POST'])
def encrypt_file_rsa():
    pass


@app.route('/encrypt/file/elgamal', methods=['POST'])
def encrypt_file_elgamal():
    pass


''' File decryption '''


@app.route('/decrypt/file/rsa', methods=['POST'])
def decrypt_file_rsa():
    pass


@app.route('/decrypt/file/elgamal', methods=['POST'])
def decrypt_file_elgamal():
    pass
