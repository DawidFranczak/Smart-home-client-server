from rest_framework.decorators import api_view
from rest_framework.response import Response
from .mod import send_data, check_aqua
# 'api/aquarium'


@api_view(['POST'])
# /aquarium/change
def aquaChange(request):
    color = request.POST.get('action')
    ip = '192.168.0.124'
    port = 7863
    # print(request.POST)
    return Response({"response": send_data(color, ip, port)})


@api_view(['POST'])
# /aquarium/check
def aquaCheck(request):
    return Response(check_aqua(request))
