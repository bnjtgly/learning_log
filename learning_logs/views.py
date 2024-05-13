from django.http import HttpResponse


def index(request):
    return HttpResponse("<h3>Welcome to Learning Log!<h3>")