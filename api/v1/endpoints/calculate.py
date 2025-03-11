#!/usr/bin/python3
"""
The API endpoint for calculating the price
"""
from api.v1.endpoints import api_endpoints
from models import storage
from models.category import Category
from models.fuel_type import FuelType
from models.manufacturer import Manufacturer
from models.model import Model


@api_endpoints.route('/calculate/<model_name>/<object_id>', strict_slashes=False)
def calculate(model_name, object_id):
    """
    Calculates the import price of the item given the model name
    and it's id
    """
    models = storage.all(Model)

    for key, value in models.items():
        obj_id = key.split(".")[1]
        if obj_id == object_id:
            price = value.calc()
            return jsonify({"price": price})

