#!/usr/bin/python3
"""
The main entry point of the application
"""
from web_flask.pages import app_pages
from web_flask.pages import web
from api.v1 import api_endpoints
from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
app.register_blueprint(app_pages)
app.register_blueprint(web)
app.register_blueprint(api_endpoints)


cors = CORS(app, resources={r"/*": {"origins": "*"}})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
