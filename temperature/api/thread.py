from datetime import datetime
import requests
import json

from const.urls import SERVER_URL, CLIENT_URL, TEMPERATURE_GET_ALL, TEMPERATURE_UPDATE
from .mod import measurement


def tempCheck():
    hour_old = datetime.now().hour
    # while True:
    for i in range(1):
        hour_now = datetime.now().hour
        # if hour_old != hour_now:
        if True:
            data = {"url": CLIENT_URL}
            sensors = requests.get(
                SERVER_URL + TEMPERATURE_GET_ALL, params=data)
            sensors = sensors.json()

            data['measurment'] = [measurement(sensor['ip'], sensor['port'])
                                  for sensor in sensors]

            headers = {'Content-Type': 'application/json',
                       'Accept': 'application/json'}

            requests.put(SERVER_URL+TEMPERATURE_UPDATE,
                         data=json.dumps(data), headers=headers)
