#!/usr/bin/python3
""" module for states query """

from api.v1.views import app_views
from flask import jsonify, abort, request
import models


@app_views.route("/states", methods=["GET"], strict_slashes=False)
def all_states():
    """Returns all the states"""
    all_state = models.storage.all("State")
    new_dict = [val.to_dict() for val in all_state.values()]
    return jsonify(new_dict)


@app_views.route("/states", methods=["POST"], strict_slashes=False)
def create_state():
    """Creates state"""
    json = request.get_json()
    State = models.state.State
    if json is not None:
        if json.get("name") is not None:
            obj = State(name=json.get("name"))
            obj.save()
            return jsonify(obj.to_dict()), 201
        else:
            abort(400, "Missing name")
    else:
        abort(400, "Not a JSON")


@app_views.route("/states/<state_id>", methods=["GET"], strict_slashes=False)
def stateId(state_id):
    """Returns the state with an id"""
    obj = models.storage.get("State", state_id)
    if obj is not None:
        return jsonify(obj.to_dict())
    else:
        abort(404)


@app_views.route("/states/<state_id>", methods=["DELETE"],
                 strict_slashes=False)
def state_del(state_id):
    """ return empty dict with 200 status"""
    obj = models.storage.get("State", state_id)
    if obj is not None:
        models.storage.delete(obj)
        models.storage.save()
        return jsonify({})
    else:
        abort(404)


@app_views.route("/states/<state_id>", methods=["PUT"], strict_slashes=False)
def update_state(state_id):
    """Returns the state with an id"""
    obj = models.storage.get("State", state_id)
    json = request.get_json()
    if obj is not None:
        if json is not None:
            for key, value in json.items():
                if key not in ["id", "updated_at", "created_at"]:
                    setattr(obj, key, value)
            obj.save()
            return jsonify(obj.to_dict())
        else:
            abort(400, "Not a JSON")
    else:
        abort(404)
