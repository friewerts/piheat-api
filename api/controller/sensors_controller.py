from http import HTTPStatus
from flask import Blueprint, jsonify

from api.service.TemperatureService import TemperatureService

sensors_controller = Blueprint('sensors_controller', __name__)

temperature_service = TemperatureService()


@sensors_controller.route('/', methods=["GET"])
def get_all_sensors():
    sensors = temperature_service.get_all_sensors()
    sensors_data = list(map(lambda x: x.data(), sensors))
    return jsonify(sensors_data), HTTPStatus.OK
