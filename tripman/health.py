from django import db
from django.http import HttpResponse


def healthcheck(request):
    db.connection.ensure_connection()
    return HttpResponse("OK")
