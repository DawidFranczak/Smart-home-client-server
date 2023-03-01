from rest_framework.decorators import api_view
from rest_framework.response import Response

from .mod import send_data, check_aqua


@api_view(['POST'])
# /aquarium/change
def aquaChange(request):
    message = request.POST.get('message')
    ip = request.POST.get('ip')
    port = int(request.POST.get('port'))
    return Response({"response": send_data(message, ip, port)})


@api_view(['POST'])
# /aquarium/check
def aquaCheck(request):
    led_start = request.POST.get('led_start')
    led_stop = request.POST.get('led_stop')
    fluo_start = request.POST.get('fluo_start')
    fluo_stop = request.POST.get('fluo_stop')
    ip = request.POST.get('ip')
    port = int(request.POST.get('port'))
    response = check_aqua(led_start, led_stop, fluo_start, fluo_stop, ip, port)
    return Response(response)
