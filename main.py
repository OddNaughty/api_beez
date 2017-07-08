import json
import time
import logging
import logging.config
from raspberry import MyPi


def launch_logger():
    with open('logging.json', 'r') as f:
        config = json.load(f)
    logging.config.dictConfig(config)

launch_logger()

logger = logging.getLogger("api_beez")


def init():
    logger.debug("Raspberry Pi initialization")
    return MyPi()


def save_datas(datas):
    with open("sensor_backup.json") as file:
        existing = json.load(file)
    print(existing)
    with open("sensor_backup.json", "w") as file:
        file.write(json.dumps({"lol": 45}, sort_keys=True, indent=2))
    return datas


def send_datas(datas):
    logger.debug(f"Sending motherfucking datas: {datas}")


def main():
    raspy = init()
    old_time = time.time()
    while True:
        new_time = time.time()
        if old_time + 2 < new_time:
            to_send = raspy.sensor_datas()
            saved = save_datas(to_send)
            sended = send_datas(to_send)
            old_time = time.time()
    return 0


if __name__ == '__main__':
    main()
