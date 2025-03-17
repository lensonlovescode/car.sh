#!/usr/bin/python3
"""
The api application running on port 5001
"""

from flask import Flask, render_template, request, jsonify
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired
import pandas as pd

from api.v1.endpoints import api_endpoints

app = Flask(__name__)
app.config['SECRET_KEY'] = 'very-secret-key'

data = {
    "Make": ["Bentley", "Bentley", "Bentley", "Ford", "Ford", "Toyota", "Toyota"],
    "Model": ["Continental GT", "Flying Spur", "Bentayga", "Mustang", "F-150", "Camry", "Corolla"],
    "Year": [2022, 2023, 2021, 2022, 2023, 2022, 2023]
}
df = pd.DataFrame(data)

def get_makes():
    return df["Make"].unique().tolist()

def get_models(make):
    return df[df["Make"] == make]["Model"].unique().tolist()

def get_years(make, model):
    return df[(df["Make"] == make) & (df["Model"] == model)]["Year"].unique().tolist()

class Fetch_Cars(FlaskForm):
    car_make = SelectField("Select Make", choices=[], validators=[DataRequired()])
    car_model = SelectField("Select Model", choices=[], validators=[DataRequired()])
    car_year = SelectField("Select Year", choices=[], validators=[DataRequired()])
    submit = SubmitField('Submit')

@api_endpoints.route('/', methods=['GET', 'POST'])
def index():
    form = Fetch_Cars()
    form.car_make.choices = [(make, make) for make in get_makes()]
    return render_template('index.html', form=form)

@api_endpoints.route('/get_models', methods=['POST'])
def get_models_route():
    make = request.form['make']
    models = get_models(make)
    return jsonify(models)

@api_endpoints.route('/get_years', methods=['POST'])
def get_years_route():
    make = request.form['make']
    model = request.form['model']
    years = get_years(make, model)
    return jsonify(years)

if __name__ == '__main__':
    app.run(debug=True)
if __name__ == '__main__':
    api.run(host='0.0.0.0', port=5001, debug=True)

