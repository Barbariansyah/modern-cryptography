from app import app
from flask import request, send_file, jsonify
from .util.create_response import create_file_response
from .util.handle_file import handle_file, handle_ascii_file
from .cipher.rsa import *


@app.route('/file')
def index_file():
    return "Hello, file!"


''' File encryption '''


@app.route('/encrypt/file/rsa', methods=['POST'])
def encrypt_file_rsa():
    file = request.files['file']
    public_key = request.form['public_key']
    filename, file_context = handle_ascii_file(file)
    encrypted_context = encrypt_rsa(file_context, public_key)

    complete_filename = create_file_response(
        filename, encrypted_context)
    return send_file(complete_filename)


@app.route('/encrypt/file/elgamal', methods=['POST'])
def encrypt_file_elgamal():
    file = request.files['file']
    key = request.form['key']
    filename, file_context = handle_file(file)
    encrypted_context = file_context  # TODO

    complete_filename = create_file_response(
        filename, encrypted_context)
    return send_file(complete_filename)


''' File decryption '''


@app.route('/decrypt/file/rsa', methods=['POST'])
def decrypt_file_rsa():
    file = request.files['file']
    private_key = request.form['private_key']
    filename, file_context = handle_ascii_file(file)
    decrypted_context = decrypt_rsa(file_context, private_key)  # TODO

    complete_filename = create_file_response(
        filename, decrypted_context)
    return send_file(complete_filename)


@app.route('/decrypt/file/elgamal', methods=['POST'])
def decrypt_file_elgamal():
    file = request.files['file']
    key = request.form['key']
    filename, file_context = handle_file(file)
    decrypted_context = file_context  # TODO

    complete_filename = create_file_response(
        filename, decrypted_context)
    return send_file(complete_filename)
