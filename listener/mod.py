import requests

from const.mod import send_data
from const.urls import CLIENT_URL, LAMP_CHECK, SERVER_URL, UID_CHECK


def check_uid(incoming_data) -> None:
    uid: str = incoming_data[0].decode("UTF-8")
    ip: str = incoming_data[1][0]
    port: str = incoming_data[1][1]
    data: dict = {
        "uid": uid,
        "ip": ip,
        "url": CLIENT_URL,
    }
    answer = requests.post(SERVER_URL + UID_CHECK, data=data, timeout=1).json()
    mess = "access" if answer["success"] else "acces-denied"
    send_data(mess, ip, port)


def check_lamp(incoming_data) -> None:
    message: str = incoming_data[0].decode("UTF-8")
    ip: str = incoming_data[1][0]
    data: dict = {
        "ip": ip,
        "url": CLIENT_URL,
    }
    answer = requests.post(SERVER_URL + LAMP_CHECK, data=data, timeout=1).json()
    send_data(message, answer["ip"], answer["port"])
