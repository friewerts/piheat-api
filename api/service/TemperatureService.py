from api.service.ConfigurationService import ConfigurationService
from api.model.TemperatureSensor import TemperatureSensor


class TemperatureService:

    configuration_service: ConfigurationService

    def __init__(self):
        self.configuration_service = ConfigurationService()

    def get_sensor_paths(self):
        return self.configuration_service.get_config("sensor_files") or []

    def get_all_sensors(self):
        return list(map(TemperatureSensor, self.get_sensor_paths()))