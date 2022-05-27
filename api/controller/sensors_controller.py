from http import HTTPStatus
from flask import Blueprint, jsonify

sensors_controller = Blueprint('sensors_controller', __name__)


@sensors_controller.route('/', methods=["GET"])
def get_all_sensors():
    sensors = ["main_sensor", "fallback_sensor"]
    return jsonify(sensors), HTTPStatus.OK
