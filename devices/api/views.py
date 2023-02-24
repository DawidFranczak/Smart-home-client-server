from rest_framework.decorators import api_view
from rest_framework.response import Response

from .mod import add_device, add_card


@api_view(['POST'])
# /api/devices/add/
def addDevice(request):
    message = str.encode(request.POST.get('message'))
    answer = request.POST.get('answer')
    port = int(request.POST.get('port'))
    return Response(add_device(message, answer, port))


@api_view(['POST'])
# /api/devices/add/card/
def addCard(request):
    ip = request.POST.get('ip')
    port = int(request.POST.get('port'))
    return Response(add_card(ip, port))
