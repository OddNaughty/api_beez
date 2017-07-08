import datetime
import logging
import json

logger = logging.getLogger("api_beez")


def save_datas(datas):
    file = open("sensor_backup.json", "r")
    try:
        existing = json.load(file)
    except json.decoder.JSONDecodeError as e:
        existing = {}
    new_entry = {datetime.datetime.now().isoformat(): datas}
    datas = {**existing, **new_entry} if existing else new_entry
    file.close()
    file = open("sensor_backup.json", "w")
    file.write(json.dumps(datas, sort_keys=True, indent=2))
    return datas


def send_datas(datas):
    logger.debug(f"Sending motherfucking datas: {datas}")
