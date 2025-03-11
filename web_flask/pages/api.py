#!/usr/bin/python3
"""
Routes for the apis to be used in fetching data
"""
from web_flask.pages import app_pages
from models import storage
from models.manufacturers import Manufacturer
from flask import jsonify


@app_pages.route('/manufacturers', strict_slashes=False)
def get_makes():
    """
    Fetches all manufacturers eg Volvo, BMW etc
    """
    makes = storage.all(Manufacturer)
    return (jsonify(makes))
