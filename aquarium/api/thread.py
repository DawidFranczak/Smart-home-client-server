from datetime import datetime
import time
import json
import requests

from .mod import check_aqua
from const.urls import SERVER_URL, CLIENT_URL, AQUARIUM_GET_ALL, AQUARIUM_UPDATE


def aquas_check():
    """Get all aquas from the server then check if they aren't up to date
    return new values fluolamp and leds"""
    old_minutes = datetime.now().minute
    while True:
        new_minutes = datetime.now().minute
        if old_minutes != new_minutes:
            try:
                data = {"url": CLIENT_URL}
                aquas = requests.post(
                    SERVER_URL + AQUARIUM_GET_ALL, data=data, timeout=1
                )
                aquas = aquas.json()
                test = [
                    check_aqua(
                        aqua["led_start"],
                        aqua["led_stop"],
                        aqua["fluo_start"],
                        aqua["fluo_stop"],
                        aqua["ip"],
                        aqua["port"],
                    )
                    for aqua in aquas
                    if not aqua["mode"]
                ]

                headers = {
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                }

                data["settings"] = test
                requests.post(
                    SERVER_URL + AQUARIUM_UPDATE,
                    data=json.dumps(data),
                    headers=headers,
                    timeout=1,
                )
                old_minutes = new_minutes
            except:
                print("No connection, next attempt in 2 seconds.")
                time.sleep(2)
        time.sleep(1)
