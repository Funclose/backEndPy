from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
import json
import logging
from django.http import JsonResponse
logger = logging.getLogger(__name__)


# def MainPage(request):
#     return render(request, 'index.html')

@api_view(["GET"])
@permission_classes([AllowAny])
def hello(request):
    return Response({"message": "Hello from Django API"})

@csrf_exempt               # только для разработки!
def echo(request):
    if request.method != "POST":
        return JsonResponse({"detail": "Only POST allowed"}, status=405)

    try:
        data = json.loads(request.body.decode("utf-8"))
    except Exception:
        return JsonResponse({"detail": "Invalid JSON"}, status=400)

    # Чтобы "увидеть" на бэке
    print("ECHO received:", data)
    logger.info("ECHO received: %s", data)

    return JsonResponse({"ok": True, "received": data}, status=201)