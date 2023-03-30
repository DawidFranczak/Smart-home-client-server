from rest_framework.decorators import api_view
from rest_framework.response import Response
from const.mod import send_data


@api_view(["PUT"])
# /api/stairs/change/
def changeStairs(request):
    message = request.data.get("message")
    ip = request.data.get("ip")
    port = int(request.data.get("port"))
    success = send_data(message, ip, port)
    status = 200 if success else 504
    return Response({}, status=status)
