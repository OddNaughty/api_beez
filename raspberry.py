import json
import logging

logger = logging.getLogger("api_beez")


class MyPi(object):
    def __init__(self):
        self.config = json.load(open("my_pi_settings.json", "r"))
        self.sensors = self.sensor_matches(self.config['sensors'])

    @classmethod
    def sensor_matches(cls, sensor_config):
        matches = {
            "DS18B20": TempSensor("DS18B20")
        }
        sensors = []
        for sensor in sensor_config:
            sensors.append(matches[sensor])
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
