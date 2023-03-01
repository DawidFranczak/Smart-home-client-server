import requests
import json
from const.urls import CLIENT_URL, SERVER_URL, UID_CHECK


def check_uid(data):
    uid = data[0].decode("UTF-8")
    ip = data[1][0]
    print(ip)
    data = {
        "uid": uid,
        "ip": ip,
        "url": CLIENT_URL,
    }
    print(SERVER_URL+UID_CHECK)
    answer = requests.post(SERVER_URL+UID_CHECK,data = data)
    print(answer.text)


def check_lamp():
    pass
