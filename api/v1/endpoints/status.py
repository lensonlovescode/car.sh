#!/usr/bin/python3
"""
Creates the status endpoint
"""
from api.v1.endpoints import api_endpoints
from flask import jsonify

@api_endpoints.route('/status', strict_slashes=False)
def get_status():
    """
    The api endpoint to check the status of the api
    """
    return jsonify({"status": "OK"})
