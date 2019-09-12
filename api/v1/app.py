#!/usr/bin/python3
"""
Module for api
"""
from flask import Flask, jsonify
import models
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)


@app.errorhandler(404)
def error_404(e):
    """Returns the status 404"""
    return jsonify({"error": "Not found"})


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    models.storage.close()

if __name__ == "__main__":
    app.run(host=getenv("HBNB_API_HOST"),
            port=int(getenv("HBNB_API_PORT")), threaded=True)
