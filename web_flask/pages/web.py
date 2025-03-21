#!/usr/bin/python3
"""
Routes for other pages
"""
from web_flask.pages import app_pages
from flask import render_template



@app_pages.route('/howto', strict_slashes=False)
def howto():
    return render_template("howto.html")

@app_pages.route('/faq', strict_slashes=False)
def faq():
    return render_template("faq.html")