import yaml

from os import path


class ConfigurationService:
    config_data: dict

    def __init__(self):
        default_config_path = path.join(path.dirname(__file__), "../config/config.yml")
        self.config_data = ConfigurationService.get_config_data(default_config_path)

    @staticmethod
    def get_config_data(config_path):
        try:
            config_stream = open(config_path, 'r')
            config_data = yaml.safe_load(config_stream)
            return config_data
        except OSError as exception:
            print(exception)
            return dict()
        except yaml.YAMLError as exc:
            print(exc)
            return dict()

    def get_config(self, name):
        return self.config_data.get(name)
