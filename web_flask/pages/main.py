#!/usr/bin/python3
"""
The routes for the main page
"""
from web_flask.pages import app_pages
from flask import render_template


@app_pages.route('/', strict_slashes=False, methods=["GET", "POST"])
def main_page():
    return render_template('index.html')


@app_pages.route('/howto', strict_slashes=False)
def howto():
    return render_template("howto.html")


@app_pages.route('/faq', strict_slashes=False)
def faq():
    return render_template("faq.html")


if __name__ == '__main__':
    app.run(debug=True)
