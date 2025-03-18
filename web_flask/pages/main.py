#!/usr/bin/python3
"""
The routes for the main page
"""
from web_flask.pages import app_pages
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired
import pandas as pd

# all_car_makes = [("volvo","Volvo"), ("bentley","Bentley"), ("toyota","Toyota"), ("tesla","Tesla")]
# all_car_model = ["GT_R", "Urban Cruiser", "CX-5"]
# all_car_year = [2000, 2005, 2019, 2014]

class Fetch_Cars(FlaskForm):
    car_make = SelectField("Select Make", choices=[], validators=[DataRequired()])
    car_model = SelectField("Select Model", choices=[], validators=[DataRequired()])
    car_year = SelectField("Select Year", choices=[], validators=[DataRequired()])
    search = SubmitField("Search")

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

# @app_pages.route('/', strict_slashes=False, methods=["GET", "POST"])
# def main_page():
#     form = Fetch_Cars()
#     if form.validate_on_submit():
#         make = form.car_make.data
#         model = form.car_model.data
#         year = form.car_model.data
#         calc = None
#         return render_template('index.html', calculations=calc)
#     return render_template('index.html', sform=form)

@app_pages.route('/', methods=['GET', 'POST'])
def index():
    form = Fetch_Cars()
    form.car_make.choices = [(make, make) for make in get_makes()]
    return render_template('index.html', sform=form)

@app_pages.route('/get_models', methods=['POST'])
def get_models_route():
    make = request.form['make']
    models = get_models(make)
    return jsonify(models)

@app_pages.route('/get_years', methods=['POST'])
def get_years_route():
    make = request.form['make']
    model = request.form['model']
    years = get_years(make, model)
    return jsonify(years)

if __name__ == '__main__':
    app.run(debug=True)
