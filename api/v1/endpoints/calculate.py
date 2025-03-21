#!/usr/bin/python3
"""
The API endpoint for calculating the price
"""
from api.v1 import api_endpoints
from models import storage
from models.category import Category
from models.fuel_type import FuelType
from models.manufacturer import Manufacturer
from models.model import Model
from flask import jsonify


@api_endpoints.route('/calculate/<model_id>', strict_slashes=False)
def calculate(model_id):
    """
    Calculates the import price of the item given the model name
    and it's id
    """
    models = storage.all(Model)

    for key, value in models.items():
        if model_id == value.id:

            price = value.calculate()
            storage.close()
            return jsonify({"price": price})
        
    storage.close()
    return (jsonify({'price': 'None'}))

