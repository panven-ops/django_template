from django.shortcuts import render
from django.db import connection
from django.db.utils import OperationalError
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def health_check(request):

    return Response({"status": "OK"})

@api_view(["GET"])
def readiness_check(request):

    try:
        connection.ensure_connection()

    except OperationalError:
        return Response({"status": "unavailable", "database": "down"})

    return Response({"status": "available", "database": "up"})
