#!/usr/bin/python3
"""
Creates blueprint for the app
"""
from flask import Blueprint


web = Blueprint('web', __name__)
app_pages = Blueprint('app_pages', __name__)


from web_flask.pages.web import *
from web_flask.pages.main import *
