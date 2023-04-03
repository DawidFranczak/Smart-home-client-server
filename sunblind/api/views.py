from rest_framework.decorators import api_view
from rest_framework.response import Response

from const.mod import send_data


@api_view(["PUT"])
def message_sunblind(request):
    """
    This function sends message to sunblind microcontrolelr

    endpoint: /api/sunblind/message/
    """

    message: str = request.data.get("message")
    ip: str = request.data.get("ip")
    port: int = int(request.data.get("port"))
    success = send_data(message, ip, port)
    status = 200 if success else 504
    return Response({}, status=status)
