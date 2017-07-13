import datetime
import logging
import requests
import urllib.parse
import json

logger = logging.getLogger("api_beez")


def send_to_somei(path, datas):
    config = json.load(open("config_settings.json", "r"))
    somei_config = config["app"]["somei"]
    to_send = {"id": config["raspberry"]["id"], "datas": datas}
    r = requests.post(urllib.parse.urljoin(somei_config["endpoint"], path), json=to_send)
    return r


def save_datas(datas):
    file = open("sensor_backup.json", "r")
    try:
        existing = json.load(file)
    except json.decoder.JSONDecodeError as e:
        existing = {}
    new_entry = {datetime.datetime.now().isoformat(): datas}
    # We could try to save them by day, with hour as key ? :o
    new_datas = {**existing, **new_entry} if existing else new_entry
    file.close()
    file = open("sensor_backup.json", "w")
    file.write(json.dumps(new_datas, sort_keys=True, indent=2))
    return datas


def send_datas(datas):
    logger.debug(f"Sending motherfucking datas: {datas}")
    return send_to_somei("/hives/", datas)
