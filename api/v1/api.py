#!/usr/bin/python3
"""
The api application running on port 5001
"""
from api.v1.endpoints import api_endpoints
from flask import Flask, jsonify
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from models.model import Model, Category, FuelType, Manufacturer  # Import your model classes

api = Flask(__name__)
api.register_blueprint(api_endpoints)


if __name__ == '__main__':
    api.run(host='0.0.0.0', port=5001, debug=True)

# !/usr/bin/python3
"""
API for fetching data from the Model table.
"""


app = Flask(__name__)

# Replace with your database connection string
DATABASE_URL = "sqlite:///./your_database.db"  # or your database connection string.

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)  # create the tables if they dont exist.

@app.route('/models', methods=['GET'])
def get_models():
    models = db.query(Model).all()
    model_list = []
    for model in models:
        model_data = {
            "id": model.id,
            "name": model.name,
            "category_id": model.category_id,
            "fuel_type_id": model.fuel_type_id,
            "manufacturer_id": model.manufacturer_id,
            "created_at": str(model.created_at),
            "updated_at": str(model.updated_at),
            "category": {"id": model.category.id, "name": model.category.name} if model.category else None,
            "fuel_type": {"id": model.fuel_type.id, "name": model.fuel_type.name} if model.fuel_type else None,
            "manufacturer": {"id": model.manufacturer.id,
                             "name": model.manufacturer.name} if model.manufacturer else None,
        }
        model_list.append(model_data)
    return jsonify(model_list)


@app.route('/models/<model_id>', methods=['GET'])
def get_model(model_id):
    model = db.query(Model).filter(Model.id == model_id).first()
    if model:
        model_data = {
            "id": model.id,
            "name": model.name,
            "category_id": model.category_id,
            "fuel_type_id": model.fuel_type_id,
            "manufacturer_id": model.manufacturer_id,
            "created_at": str(model.created_at),
            "updated_at": str(model.updated_at),
            "category": {"id": model.category.id, "name": model.category.name} if model.category else None,
            "fuel_type": {"id": model.fuel_type.id, "name": model.fuel_type.name} if model.fuel_type else None,
            "manufacturer": {"id": model.manufacturer.id,
                             "name": model.manufacturer.name} if model.manufacturer else None,
        }
        return jsonify(model_data)
    else:
        return jsonify({"message": "Model not found"}), 404


    app.run(debug=True)
