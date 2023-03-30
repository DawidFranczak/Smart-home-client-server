from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .mod import change_light


@api_view(["PUT"])
def toggle_light(request):
    ip: str = request.data["ip"]
    port: int = int(request.data["port"])
    message = change_light(ip, port)

    if message["result"]:
        return Response(message, status=status.HTTP_200_OK)

    return Response(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
