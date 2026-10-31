from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def health(request):
    return Response({"status": "ok"})


@api_view(["GET"])
def hello(request):
    name = request.query_params.get("name", "World")
    return Response({"message": f"Hello, {name}!"})
