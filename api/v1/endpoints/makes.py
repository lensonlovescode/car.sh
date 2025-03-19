#!/usr/bin/python3
"""
API endpoint for fetching makes
"""
from api.v1 import api_endpoints
from models import storage
from models.manufacturer import Manufacturer
from flask import jsonify

@api_endpoints.route('/makes', strict_slashes=False)
def get_models_route():
    """
    Method for fetching models
    """
    my_dict = storage.all(Manufacturer)
    my_list = []

    for k, v in my_dict.items():
        my_list.append(v.to_dict())

    return jsonify(my_list)
