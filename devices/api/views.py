from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .mod import add_card, add_device


@api_view(["POST"])
# /api/devices/add/
def add_new_device(request):
    """
    This function is for adding new devices

    endpoint:/api/devices/add/
    """

    message: str = str.encode(request.POST.get("message"))
    answer: str = request.POST.get("answer")
    port: int = int(request.POST.get("port"))
    response = add_device(message, answer, port)

    if response["success"]:
        return Response(response, status=status.HTTP_200_OK)
    return Response({}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["POST"])
# /api/devices/add/card/
def add_new_card(request):
    """
    This function is for adding new rfid cards

    endpoint:/api/devices/add/
    """
    ip = request.POST.get("ip")
    port = int(request.POST.get("port"))
    response = add_card(ip, port)

    if response["success"]:
        return Response(response, status=status.HTTP_200_OK)
    return Response({}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
