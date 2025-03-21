#!/usr/bin/python3
"""
The routes for the discover page
"""
from web_flask.pages import app_pages
from flask import render_template


@app_pages.route('/discover', strict_slashes=False)
def discover_page():
    return render_template('discover.html')
