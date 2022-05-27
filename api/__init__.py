import json
from http import HTTPStatus

from flask import Flask, jsonify

from api.controller.sensors_controller import sensors_controller

api = Flask(__name__)

api.register_blueprint(sensors_controller, url_prefix='/sensors/')


def start_api():
    api.run(debug=True, port=5000)

