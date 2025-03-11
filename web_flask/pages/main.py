#!/usr/bin/python3
"""
The routes for the main page
"""
from web_flask.pages import app_pages
from flask import render_template


@app_pages.route('/', strict_slashes=False)
def main_page():
    """
    The route for the main page
    """
    return render_template('index.html')
