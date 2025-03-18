#!/usr/bin/python3
"""
The api application running on port 5001
"""

from flask import Flask
from api.v1 import api_endpoints
from flask_cors import CORS


app = Flask(__name__)
app.register_blueprint(api_endpoints)

cors = CORS(app, resources={r"/*": {"origins": "*"}})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)