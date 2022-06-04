from pathlib import Path
from dataclasses import dataclass, field


@dataclass
class TemperatureSensor:
    path: str
    name: str = field(init=False)

    def __post_init__(self):
        self.name = Path(self.path).stem

    def get_temperature(self) -> float:
        file = open(self.path, "r")
        file_content = file.read()
        temp_str = file_content.split('\n')[1].split(' ')[9]
        return float(temp_str[2:]) / 1000

    def data(self):
        return {
            "name": self.name,
            "temperature": self.get_temperature()
        }
