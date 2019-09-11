#!/usr/bin/python3
"""
Module for index
"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route("/status")
def status():
    """Returns the status OK"""
    return jsonify({"status": "OK"})
