from django import db
from django.http import HttpResponse


def warmup(request):
    db.connection.ensure_connection()
    return HttpResponse("OK")
