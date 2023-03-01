import requests
from const.urls import CLIENT_URL, SERVER_URL, UID_CHECK, LAMP_CHECK

from const.mod import send_data

def check_uid(data):
    uid = data[0].decode("UTF-8")
    ip = data[1][0]
    port = data[1][1]
    data = {
        "uid": uid,
        "ip": ip,
        "url": CLIENT_URL,
    }
    answer = requests.post(SERVER_URL+UID_CHECK,data = data).json()
    mess = "access" if answer["success"] else "acces-denied"
    send_data(mess,ip,port)


def check_lamp(data):
    message = data[0].decode("UTF-8")
    ip = data[1][0]
    data = {
        "ip": ip,
        "url": CLIENT_URL,
    }
    answer = requests.post(SERVER_URL+LAMP_CHECK,data = data).json()
    send_data(message,answer["ip"],answer["port"])
