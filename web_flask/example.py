#!/usr/bin/python3
"""
An illustration for how a flask application runs
"""
from flask import Flask, render_template


app = Flask(__name__)



@app.route('/example', strict_slashes=False)
def example():
    return render_template('example.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
