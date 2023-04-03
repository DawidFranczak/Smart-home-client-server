import socket
from datetime import datetime


def send_data(command: str, ip: str, port: int) -> bool:
    """
    This function sends command to the microcontroller.

    :params command: This is command for the microcontroller.
    :params ip: This is microcontroller's ip.
    :params port: This is microcontroller port

    :return: True if communication with microcontroller successfully
    """

    try:
        wiad = str.encode(command)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(wiad, (ip, port))
        sock.settimeout(0.5)
        sock.recvfrom(128)
        sock.close()
        return True
    except TimeoutError:
        sock.close()
        return False


def check_aqua(request: object) -> dict:
    """
    This function check time and depend on it send command
    to microcontroller about turn on/off led and fluorescent lamp

    :params request: This is incoming request from main server. In request's body
    should be dictionary like below
    {
        "led_start" : "00:00:00" // hh:mm:ss
        "led_stop" : "00:00:00" // hh:mm:ss
        "fluo_start" : "00:00:00" // hh:mm:ss
        "fluo_stop" : "00:00:00" // hh:mm:ss
        "ip" : "192.168.0.xxx" // last octet shoud be given by DHCP server
        "port" : "xxxx"
    }

    :return: If either (led and fluorescent lamp) will be check
    and communication with the microcontroller will proceed successfully
    they return dictionary like below
    {
        "response": True,
        "fluo_mode": fluo_mode, // (True -> turn on or False -> turn off)
        "led_mode": led_mode, // (True -> turn on or False -> turn off)
        "ip": ip, // microcontroller's ip
    }
    """

    led_start: str = request.POST.get("led_start")
    led_stop: str = request.POST.get("led_stop")
    fluo_start: str = request.POST.get("fluo_start")
    fluo_stop: str = request.POST.get("fluo_stop")
    ip: str = request.POST.get("ip")
    port: int = int(request.POST.get("port"))

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
        return {"success": False}

    if fluo_start < time_now < fluo_stop:
        fluo = "s1"
        fluo_mode = True
    else:
        fluo = "s0"
        fluo_mode = False

    if not send_data(fluo, ip, port):
        return {"success": False}
    return {
        "success": True,
        "fluo_mode": fluo_mode,
        "led_mode": led_mode,
        "ip": ip,
    }
