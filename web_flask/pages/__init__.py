#!/usr/bin/python3
"""
Creates blueprint for the app
"""
from flask import Blueprint


app_pages = Blueprint('app_pages', __name__, url_prefix='/')


from web_flask.pages.web import *
from web_flask.pages.main import *
from web_flask.pages.discover import *
