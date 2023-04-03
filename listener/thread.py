import socket
import threading
import time

from const.commands import LISNER_PORT

from .mod import check_lamp, check_uid


def listener() -> None:
    """
    This function receives commands from microcontrollers.
    """

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(("", LISNER_PORT))

    while True:
        try:
            sock.settimeout(0.5)
            data_rec = sock.recvfrom(1024)
            message = data_rec[0].decode("UTF-8")
            if message:
                match message:
                    case ("still" | "click" | "RFID"):
                        message: str = message[0].decode("UTF-8")
                        ip: str = message[1][0]
                        check_lamp(message, ip)
                    case _:
                        try:
                            UID = int(message)
                            if type(UID) == int:
                                uid: str = message[0].decode("UTF-8")
                                ip: str = message[1][0]
                                port: str = message[1][1]
                                check_uid(uid, ip, port)
                        except:
                            print("Unrecognized command.")
        except:
            if not threading.main_thread().is_alive():
                sock.close()
                break
        time.sleep(0.5)
