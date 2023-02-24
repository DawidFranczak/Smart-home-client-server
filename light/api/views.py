from rest_framework.decorators import api_view
from rest_framework.response import Response
from .mod import change_light


@api_view(['PUT'])
def changeLight(request):
    ip = request.data["ip"]
    port = int(request.data["port"])
    return Response(change_light(ip, port))
