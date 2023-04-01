from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .mod import check_aqua, send_data


@api_view(["POST"])
# /aquarium/change
def aqua_change(request):
    message: str = request.POST.get("message")
    ip: str = request.POST.get("ip")
    port: int = int(request.POST.get("port"))

    if send_data(message, ip, port):
        return Response({"response": True}, status=status.HTTP_200_OK)
    return Response({"response": False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["POST"])
# /aquarium/check
def aqua_check(request):
    response = check_aqua(request.POST)

    if response["response"]:
        return Response(response, status=status.HTTP_200_OK)
    return Response({"response": False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
