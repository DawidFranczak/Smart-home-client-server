import socket
from const.commands import CHANGE_LIGHT


def change_light(ip: str, port: int) -> dict:
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
