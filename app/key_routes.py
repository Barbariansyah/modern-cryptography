from app import app
from flask import request


@app.route('/key')
def index_key():
    return "Hello, key!"

''' Key generation '''


@app.route('/session-key', methods=['POST'])
def generate_session_key():
    pass