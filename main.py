import json
import time
import logging
import logging.config
import rasp_data
from raspberry import MyPi


def launch_logger():
    with open('logging.json', 'r') as f:
        config = json.load(f)
    logging.config.dictConfig(config)


def init():
    launch_logger()
    logger = logging.getLogger("api_beez")
    logger.debug("Raspberry Pi initialization")
    return MyPi()


def main():
    raspy = init()
    old_time = time.time()
    while True:
        new_time = time.time()
        if old_time + 2 < new_time:
            to_send = raspy.sensor_datas()
            saved = rasp_data.save_datas(to_send)
            sended = rasp_data.send_datas(to_send)
            old_time = time.time()
    # return 0

if __name__ == '__main__':
    main()
