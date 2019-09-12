#!/usr/bin/python3
""" module for states query """

from api.v1.views import app_views
from flask import jsonify
import models


@app_views.route("/states", methods=["GET"])
def all_states():
    """Returns all the states"""
    all_state = models.storage.all("State")
    new_dict = [val.to_dict() for val in all_state.values()]
    return jsonify(new_dict)

@app_views.route("/states/<state_id>", methods=[""])
def stateId(state_id):
    """Returns the state with an id"""
    obj = models.storage.get("State", state_id)
    if obj is not None:
        return jsonify(obj.to_dict)
        
