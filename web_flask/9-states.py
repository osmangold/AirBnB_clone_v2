#!/usr/bin/python3
"""Flask app to generate html list of all states from storage"""
from flask import Flask, render_template
from models import storage
app = Flask('web_flask')
app.url_map.strict_slashes = False
