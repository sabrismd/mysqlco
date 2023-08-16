from django.http import HttpResponse
from django.db import connection

def check_connection(request):
    try:
        connection.connect()
        return HttpResponse("<h1>Database connection successful!</h1>")
    except Exception as e:
        return HttpResponse("<h1>Database connection failed</h1>")
