#!/usr/bin/python3
""" module for places query """

from api.v1.views import app_views
from flask import jsonify, abort, request
import models


@app_views.route("/cities/<city_id>/places",
                 methods=["GET"], strict_slashes=False)
def all_pofc(city_id):
    """Returns all Place objects of a City"""
    obj = models.storage.get("City", city_id)
    if obj is None:
        abort(404)
    new_dict = [val.to_dict() for val in obj.places]
    return jsonify(new_dict)


@app_views.route("/cities/<city_id>/places",
                 methods=["POST"], strict_slashes=False)
def create_place(city_id):
    """Creates place"""
    obj_city = models.storage.get("City", city_id)
    if obj_city is None:
        abort(404)
    json = request.get_json()
    Place = models.place.Place
    if json is not None:
        if json.get("user_id") is not None:
            obj_user = models.storage.get("User",
                                          json.get("user_id"))
            if obj_user is None:
                abort(404)
            if json.get("name") is not None:
                obj = Place(name=json.get("name"),
                            user_id=json.get("user_id"),
                            city_id=city_id)
                obj.save()
                return jsonify(obj.to_dict()), 201
            else:
                abort(400, "Missing name")
        else:
            abort(400, "Missing user_id")
    else:
        abort(400, "Not a JSON")


@app_views.route("/places/<place_id>", methods=["GET"], strict_slashes=False)
def placeId(place_id):
    """Returns the place with an id"""
    obj = models.storage.get("Place", place_id)
    if obj is not None:
        return jsonify(obj.to_dict())
    else:
        abort(404)


@app_views.route("/places/<place_id>", methods=["DELETE"],
                 strict_slashes=False)
def place_del(place_id):
    """ return empty dict with 200 status"""
    obj = models.storage.get("Place", place_id)
    if obj is not None:
        models.storage.delete(obj)
        models.storage.save()
        return jsonify({})
    else:
        abort(404)


@app_views.route("/places/<place_id>", methods=["PUT"], strict_slashes=False)
def update_place(place_id):
    """Returns the place with an id"""
    obj = models.storage.get("Place", place_id)
    json = request.get_json()
    if obj is not None:
        if json is not None:
            for key, value in json.items():
                if key not in ["id", "updated_at", "created_at",
                               "user_id", "city_id"]:
                    setattr(obj, key, value)
            obj.save()
            return jsonify(obj.to_dict())
        else:
            abort(400, "Not a JSON")
    else:
        abort(404)

@app_views.route("/places_search",
                 methods=["POST"], strict_slashes=False)
def search_places():
    """Searches for places"""
    json = request.get_json()
    if json is None:
        abort(400, "Not a JSON")
    all_places = models.storage.all("Place")
    list_places = [val.to_dict() for val in all_places.values()]
    if json == False:
        return jsonify(list_places)
    list_json = [len(val) for val in json.values()]
    if not any(list_json) == True:
        return jsonify(list_places)
    if json.get("State") is not None:
        if len(json.get("State")) != 0:
            for json.get("State")
            return jsonify()
