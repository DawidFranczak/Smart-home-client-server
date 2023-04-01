from const.mod import send_data
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["PUT"])
# /api/stairs/change/
def change_stairs(request):
    message: str = request.data.get("message")
    ip: str = request.data.get("ip")
    port: int = int(request.data.get("port"))
    success = send_data(message, ip, port)
    status = 200 if success else 504
    return Response({}, status=status)
