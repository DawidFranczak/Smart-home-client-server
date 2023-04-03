import requests

from const.mod import send_data
from const.urls import CLIENT_URL, LAMP_CHECK, SERVER_URL, UID_CHECK


def check_uid(uid, ip, port) -> None:
    """
    This function sends the UID of a card to the main server and waits for
    a response.Depending on the server's answer, it will send a command to
    open or not open the gate.

    :params uid:
    :params ip:
    :params port:
    """

    data: dict = {
        "uid": uid,
        "ip": ip,
        "url": CLIENT_URL,
    }
    answer = requests.post(SERVER_URL + UID_CHECK, data=data, timeout=1).json()
    mess = "access" if answer["success"] else "acces-denied"
    send_data(mess, ip, port)


def check_lamp(message, ip) -> None:
    """
    This function sends microcontroller's ip to the main server
    and get lamp's microcontroller ip and port connected with first microcontroller
    (rpl side on webside)

    :params message: This is message whith shoud be sends to lamp's microcontroller
    :params ip: This is ip address microcontroller
    """

    data: dict = {
        "ip": ip,
        "url": CLIENT_URL,
    }
    answer = requests.post(SERVER_URL + LAMP_CHECK, data=data, timeout=1).json()
    send_data(message, answer["ip"], answer["port"])
