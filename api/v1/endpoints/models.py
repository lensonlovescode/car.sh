#!/usr/bin/python3
"""
API endpoint for fetching makes
"""
from api.v1 import api_endpoints
from models import storage
from models.manufacturer import Manufacturer
from models.category import Category
from models.model import Model
from flask import jsonify


@api_endpoints.route('makes/<make>/<category>', strict_slashes=False)
def get_spec_models(make, category):
    """
    Gets model filter results based on make and category
    """
    makes = storage.all(Manufacturer)
    for k, v in makes.items():
        if make == v.name:
            make_id = v.id
            break

    print(make_id)

    categories = storage.all(Category)
    for k, v in categories.items():
        if category == v.name:
            category_id = v.id
            break

    print(category_id)

    my_list = []

    for k, v in storage.all(Model).items():
        if v.manufacturer_id == make_id and v.category_id == category_id:
            my_list.append(v.to_dict())

    storage.close()
    return(jsonify(my_list))

@api_endpoints.route('/models', strict_slashes=False)
def get_all_models():
    """
    API endpoint to get all models
    """

    my_list = []
    models = storage.all(Model)

    for k, v in models.items():
        my_list.append(v.to_dict())

    storage.close()
    return(jsonify(my_list))

# @api_endpoints.route('/models/<model_id>', strict_slashes=False)
# def get_single_model_car(model_id):
#     my_list = []

#     models = storage.all(Model)
#     for k, v in models.items():
#         my_list.append(v.to_dict())
    