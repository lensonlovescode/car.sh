#!/usr/bin/python3
"""
The main entry point of the application
"""
from web_flask.pages import app_pages
from flask import Flask


app = Flask(__name__)
app.register_blueprint(app_pages)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
