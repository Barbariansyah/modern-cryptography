from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

from app import text_routes, file_routes, key_routes