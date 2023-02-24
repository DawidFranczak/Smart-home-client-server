from rest_framework.decorators import api_view
from rest_framework.response import Response
from const.mod import send_data


@api_view(['PUT'])
# /api/sunblind/message/
def messageSunblind(request):
    message = str.encode(request.data.get('message'))
    ip = request.data.get('ip')
    port = int(request.data.get('port'))
    return Response(send_data(message, ip, port))
