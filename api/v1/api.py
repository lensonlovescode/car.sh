#!/usr/bin/python3
"""
The api application running on port 5001
"""
from flask import Flask
from api.v1.endpoints import api_endpoints

api = Flask(__name__)
api.register_blueprint(api_endpoints)


if __name__ == '__main__':
    api.run(host='0.0.0.0', port=5001, debug=True)
