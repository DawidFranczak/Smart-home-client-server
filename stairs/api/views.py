from rest_framework.decorators import api_view
from rest_framework.response import Response
from .mod import send_data


@api_view(['PUT'])
# /api/stairs/change/
def changeStairs(request):
    message = str.encode(request.data.get('message'))
    ip = request.data.get('ip')
    port = int(request.data.get('port'))
    return Response(send_data(message, ip, port))
