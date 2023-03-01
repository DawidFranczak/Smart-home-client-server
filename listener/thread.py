import socket

from .mod import check_uid, check_lamp
from const.commands import LISNER_PORT

def listener():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("", LISNER_PORT))
    print("start2")
    # sock.close()

    while (True):
        data_rec = sock.recvfrom(1024)
        message = data_rec[0].decode("UTF-8")
        # print(message)
        if message:
            match message:
                case ("still" | "click" | "RFID"):
                    check_lamp(data_rec)
                case _:
                    # try:
                        UID = int(message)
                        if type(UID) == int:
                            check_uid(data_rec)
                    # except:
                        # print("Nierozpoznana komenda")
