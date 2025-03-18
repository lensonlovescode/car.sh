#!/usr/bin/python3
"""
API endpoint for fetching categories
"""
from api.v1 import api_endpoints
from models import storage
from models.category import Category
from flask import jsonify

@api_endpoints.route('/categories', strict_slashes=False)
def get_categories():
    """
    Method for fetching models
    """
    my_dict = storage.all(Category)
    my_list = []

    for k, v in my_dict.items():
        my_list.append(v.to_dict())

    return jsonify(my_list)