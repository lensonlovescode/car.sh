#!/usr/bin/python3
"""
The routes for the main page
"""
from web_flask.pages import app_pages
from web_flask.pages import web
from flask import render_template


@app_pages.route('/', strict_slashes=False, methods=["GET", "POST"])
def main_page():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)
