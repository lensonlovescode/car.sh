#!/usr/bin/python3
"""
The main entry point of the application
"""
from web_flask.pages import app_pages
from web_flask.pages import web
from flask import Flask


app = Flask(__name__)
app.config['SECRET_KEY'] = "verysecretpassword"
app.register_blueprint(app_pages)
app.register_blueprint(web)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
