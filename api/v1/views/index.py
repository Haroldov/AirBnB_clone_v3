#!/usr/bin/python3
"""
Module for index
"""
from api.v1.views import app_views
from flask import jsonify
import models

@app_views.route("/status")
def status():
    """Returns the status OK"""
    return jsonify({"status": "OK"})

@app_views.route("/stats")
def stats():
    """Returns the stats"""
    classes = ["Amenity", "City", "User", "Place", "Review", "State"]
    new_dict = map(lambda name: (name, models.storage.count(name)), classes)
    return jsonify(dict(new_dict))
