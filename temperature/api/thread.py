import json
import time
from datetime import datetime

import requests
from const.urls import (CLIENT_URL, SERVER_URL, TEMPERATURE_GET_ALL,
                        TEMPERATURE_UPDATE)

from .mod import measurement


def temp_check() -> None:
    hour_old = datetime.now().hour
    while True:
        hour_now = datetime.now().hour
        if hour_old != hour_now:
            try:
                data = {"url": CLIENT_URL}
                sensors = requests.get(
                    SERVER_URL + TEMPERATURE_GET_ALL, params=data, timeout=1
                )
                sensors = sensors.json()

                data["measurment"] = [
                    measurement(sensor["ip"], sensor["port"]) for sensor in sensors
                ]

                headers = {
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                }

                requests.put(
                    SERVER_URL + TEMPERATURE_UPDATE,
                    data=json.dumps(data),
                    headers=headers,
                    timeout=1,
                )
                hour_old = hour_now
            except TimeoutError:
                print("Brak połączenia natępna próba za 1s")
                time.sleep(1)
        time.sleep(1)
