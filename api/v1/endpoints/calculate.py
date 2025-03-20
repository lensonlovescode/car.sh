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


@api_endpoints.route('/calculate/<model_name>', strict_slashes=False)
def calculate(model_name, object_id):
    """
    Calculates the import price of the item given the model name
    and it's id
    """
    models = storage.all(Model)

    for key, value in models.items():
        if model_name == value.name:
            price = value.calc()
            storage.close()
            return jsonify({"price": price})
        
    storage.close()
    return (jsonify({'price': 'None'}))

