#!/usr/bin/python3
"""
Creates the api blueprints
"""
from flask import Blueprint

api_endpoints = Blueprint('api_endpoints', __name__, url_prefix='/api/v1')

from api.v1.endpoints.status import *
from api.v1.endpoints.makes import *
from api.v1.endpoints.categories import *
from api.v1.endpoints.models import *
from api.v1.endpoints.calculate import *
