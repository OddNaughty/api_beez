import json
import logging

logger = logging.getLogger("api_beez")


class MyPi(object):
    # 'magic method' propre à toutes les classes (ca commence et finit par '__').
    # En l'occurence init prend des parametres et permet de les relier à l'instance via self
    def __init__(self):
        self.config = json.load(open("config_settings.json", "r"))
        self.sensors = self.sensor_matches(self.config['raspberry']['sensors'])

    # Décorateur qui permet de faire des méthodes classe et non d'instance
    @classmethod
    def sensor_matches(cls, sensor_config):
        matches = {
            "DS18B20": TempSensor("DS18B20")
        }
        sensors = []
        for sensor in sensor_config:
            sensors.append(matches[sensor])
        # La ligne en dessous permet de faire la meme chose que la boucle au dessus: -> List Comprehension
        # sensors = [matches[sensor] for sensor in sensor_config]
        return sensors

    def get_sensors(self):
        return self.sensors

    def sensor_datas(self):
        return [{sensor.name: sensor.get_data()} for sensor in self.sensors]


class Sensor(object):
    def __init__(self, name, *args, **kwargs):
        self.name = name

    def get_data(self):
        pass


class TempSensor(Sensor):
    def __init__(self, name, *args, **kwargs):
        logger.debug(f'Temp Sensor {name} just initialized')
        # print(f"Temp Sensor {name} just initialized")
        super().__init__(name, *args, **kwargs)

    def get_data(self):
        return 0
