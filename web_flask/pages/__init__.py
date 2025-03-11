#!/usr/bin/python3
"""
Creates blueprint for the app
"""
from flask import Blueprint

app_pages = Blueprint('app_pages', __name__)

from web_flask.pages.main import *
