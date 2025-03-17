#!/usr/bin/python3
"""
The api application running on port 5001
"""
from api.v1.endpoints import api_endpoints
from flask import Flask, jsonify
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from models.model import Model, Category, FuelType, Manufacturer
from flask_wtf import FlaskForm
from wtforms import SelectField
from wtforms.validators import DataRequired

api = Flask(__name__)
api.register_blueprint(api_endpoints)



if __name__ == '__main__':
    api.run(host='0.0.0.0', port=5001, debug=True)

