import socket
from const.commands import CHANGE_LIGHT


def change_light(ip, port):
    try:
        sock = socket.socket(
            socket.AF_INET, socket.SOCK_DGRAM)  # INTERNET / UDP
        sock.sendto(CHANGE_LIGHT, (ip, port))
        sock.settimeout(1)
        data = sock.recvfrom(128)
        data = data[0].decode('UTF-8')
        response = {"success": True,
                    "result": data}

    except Exception as e:
        response = {"success": False}

    finally:
        sock.close()
        return response
