import socket

from const.commands import ADD_UID


def add_device(message: str, answer: str, port: int) -> dict:
    """
    This function searches the local network for microcontroller with
    a specific IP address range (192.168.0.2 - 192.168.0.253) and specific port.

    :params message: This is message for microcontroller (they shoud be a password)
    :params answer: This is answer from microcontroller on our message.
    :params port: This is the port under which the IP addresses will be scanned

    :return:If the microcontroller is found and its response is correct,
    the function will return a dictionary like below
    {
        "success": True,
        "ip": new_sensor_ip,
    }
    """
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
    """
    This function sends a command to the RFID sensor
    to add a new card and waits for a new UID.

    :params ip: This is the IP address of the RFID sensor
    :params port: This is the port of the RFID sensor

    :return: If uid read successfully return dictionary like below
    {
        "success": True,
        "uid": uid
    }
    """

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:

        sock.sendto(ADD_UID, (ip, port))
        sock.settimeout(1)
    except TimeoutError:
        sock.close()
        return {"success": False}

    data = sock.recvfrom(128)
    uid = int(data[0].decode("UTF-8"))
    return {"success": True, "uid": uid}
