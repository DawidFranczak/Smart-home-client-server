import socket
from datetime import datetime


def send_data(mess, ip, port):
    '''
    Send message to microcontroler on port and ip  and waiting for response
    '''

    try:
        wiad = str.encode(mess)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(wiad, (ip, port))
        sock.settimeout(0.5)
        sock.recvfrom(128)
        sock.close()
        return True
    except:
        sock.close()
        return False


def check_aqua(led_start, led_stop, fluo_start, fluo_stop, ip, port):
    '''
    Turn on or turn off fluo lamp and led dependence on time
    and save it to database
    '''

    if datetime.now().hour < 10:
        hours = '0' + str(datetime.now().hour)
    else:
        hours = str(datetime.now().hour)

    if datetime.now().minute < 10:
        minutes = ':0' + str(datetime.now().minute) + \
            ':' + str(datetime.now().second)
    else:
        minutes = ':' + str(datetime.now().minute) + \
            ':' + str(datetime.now().second)

    time_now = hours + minutes

    if led_start < time_now and led_stop > time_now:
        led = 'r1'
        led_mode = True
    else:
        led = 'r0'
        led_mode = False

    if not send_data(led, ip, port):
        return {'response': False}

    if fluo_start < time_now and fluo_stop > time_now:
        fluo = 's1'
        fluo_mode = True
    else:
        fluo = 's0'
        fluo_mode = False

    if not send_data(fluo, ip, port):
        return {'response': False}
    return {
        'response': True,
        'fluo_mode': fluo_mode,
        'led_mode': led_mode,
        'ip': ip,
    }
