import socket


def measurement(ip, port, mess="pomiar") -> dict:
    """
    Send message to microcontroler on port and ip  and waiting for response
    """
    try:
        wiad = str.encode(mess)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(wiad, (ip, port))
        sock.settimeout(0.5)
        measurement = sock.recvfrom(128)
        sock.close()
        return {"success": True, "ip": ip, "temp": measurement[0].decode("utf-8")}
    except:
        sock.close()
        return {
            "success": False,
            "ip": ip,
        }
