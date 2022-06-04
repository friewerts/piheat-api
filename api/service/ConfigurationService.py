import yaml
from dotenv import load_dotenv

from os import path, getenv


class ConfigurationService:
    default_config_data: dict
    custom_config_data: dict

    def __init__(self):
        default_config_path = path.join(path.dirname(__file__), "../config/default_config.yml")
        self.default_config_data = ConfigurationService.get_config_data(default_config_path)
        self.custom_config_data = ConfigurationService.get_custom_config_data()

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

    @staticmethod
    def get_custom_config_data():
        load_dotenv()
        custom_config_path = getenv("CUSTOM_CONFIG_PATH")
        if custom_config_path is None:
            return dict()
        return ConfigurationService.get_config_data(custom_config_path)

    def get_config(self, name):
        return self.custom_config_data.get(name) or self.default_config_data.get(name)
