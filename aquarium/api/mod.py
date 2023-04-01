import socket
from datetime import datetime


def send_data(mess: str, ip: str, port: int) -> bool:
    """
    Send message to microcontroler on port and ip  and waiting for response
    """

    try:
        wiad = str.encode(mess)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(wiad, (ip, port))
        sock.settimeout(0.5)
        sock.recvfrom(128)
        sock.close()
        return True
    except TimeoutError:
        sock.close()
        return False


def check_aqua(request_post) -> dict:
    """
    Turn on or turn off fluo lamp and led dependence on time
    and save it to database
    """
    led_start: str = request_post.get("led_start")
    led_stop: str = request_post.get("led_stop")
    fluo_start: str = request_post.get("fluo_start")
    fluo_stop: str = request_post.get("fluo_stop")
    ip: str = request_post.get("ip")
    port: int = int(request_post.get("port"))

    hour: int = datetime.now().hour
    hours: str = str(hour) if hour > 9 else "0" + str(hour)

    minute = datetime.now().minute
    minutes = str(minute) if minute > 9 else "0" + str(minute)

    time_now = hours + minutes

    if led_start < time_now < led_stop:
        led = "r1"
        led_mode = True
    else:
        led = "r0"
        led_mode = False

    if not send_data(led, ip, port):
        return {"response": False}

    if fluo_start < time_now < fluo_stop:
        fluo = "s1"
        fluo_mode = True
    else:
        fluo = "s0"
        fluo_mode = False

    if not send_data(fluo, ip, port):
        return {"response": False}
    return {
        "response": True,
        "fluo_mode": fluo_mode,
        "led_mode": led_mode,
        "ip": ip,
    }
