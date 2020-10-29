from app import app
from flask import request, send_file, jsonify
from .util.create_response import create_file_response, create_file_url_response
from .util.handle_file import handle_file, handle_ascii_file
from .cipher.elgamal import encrypt_elgamal, decrypt_elgamal
from .cipher.rsa import *
import time
import os


@app.route('/file')
def index_file():
    return "Hello, file!"


''' File encryption '''


@app.route('/encrypt/file/rsa', methods=['POST'])
def encrypt_file_rsa():
    file = request.files['file']
    public_key = request.form['public_key']
    filename, file_context = handle_ascii_file(file)

    start_time = time.time()
    encrypted_context = encrypt_rsa(file_context, public_key)
    time_needed = time.time() - start_time

    complete_filename = create_file_response(
        filename, encrypted_context)

    file_size = os.stat(complete_filename).st_size

    return create_file_url_response(complete_filename, file_size)


@app.route('/encrypt/file/elgamal', methods=['POST'])
def encrypt_file_elgamal():
    file = request.files['file']
    key = request.form['key']
    filename, file_context = handle_ascii_file(file)

    start_time = time.time()
    encrypted_context = encrypt_elgamal(file_context, key)
    time_needed = time.time() - start_time

    complete_filename = create_file_response(
        filename, encrypted_context)

    file_size = os.stat(complete_filename).st_size

    return create_file_url_response(complete_filename, file_size)


''' File decryption '''


@app.route('/decrypt/file/rsa', methods=['POST'])
def decrypt_file_rsa():
    file = request.files['file']
    private_key = request.form['private_key']
    filename, file_context = handle_ascii_file(file)

    start_time = time.time()
    decrypted_context = decrypt_rsa(file_context, private_key)
    time_needed = time.time() - start_time

    complete_filename = create_file_response(
        filename, decrypted_context)

    file_size = os.stat(complete_filename).st_size

    return create_file_url_response(complete_filename, file_size)


@app.route('/decrypt/file/elgamal', methods=['POST'])
def decrypt_file_elgamal():
    file = request.files['file']
    key = request.form['key']
    filename, file_context = handle_ascii_file(file)
    file_context = file_context.decode()

    start_time = time.time()
    decrypted_context = decrypt_elgamal(file_context, key)
    time_needed = time.time() - start_time

    complete_filename = create_file_response(
        filename, decrypted_context)

    file_size = os.stat(complete_filename).st_size

    return create_file_url_response(complete_filename, file_size)
