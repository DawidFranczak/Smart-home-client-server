import socket

from const.commands import ADD_UID


def add_device(message: str, answer: str, port: int) -> dict:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    for i in range(2, 254):
        check_ip = "192.168.0." + str(i)

        try:
            sock.sendto(message, (check_ip, port))
            sock.settimeout(0.05)
            data = sock.recvfrom(128)
            response = data[0].decode("UTF-8")
            if response == answer:
                new_sensor_ip = str(data[1][0])
                sock.close()

                return {
                    "success": True,
                    "ip": new_sensor_ip,
                }

        except TimeoutError:
            continue

    sock.close()
    return {
        "success": False,
    }


def add_card(ip: str, port: int) -> dict:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(ADD_UID, (ip, port))
        sock.settimeout(1)
        data = sock.recvfrom(128)
        uid = int(data[0].decode("UTF-8"))
        return {"success": True, "uid": uid}

    except TimeoutError:
        sock.close()
        return {"success": False}
