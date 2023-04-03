import socket

from const.commands import CHANGE_LIGHT


def change_light(ip: str, port: int) -> dict:
    """
    This function sends information to the microcontroller of the
    lamp to toggle the light on or off

    :params ip: This is the IP address of the microcontroller
    :params port: This is the port of the microcontroller

    :return: dictionary like below if communication successfully
        {
            "result" : data (True-> turn on, False-> turn off)
        }
        otherwise
        {
            "result" : ""
        }
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(CHANGE_LIGHT, (ip, port))
        sock.settimeout(1)
        data = sock.recvfrom(128)
        data = data[0].decode("UTF-8")
        sock.close()

        return {"result": data}

    except TimeoutError:
        sock.close()
        return {"result": ""}
