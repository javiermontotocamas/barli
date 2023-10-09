from django.shortcuts import HttpResponse


def index(request):
    return HttpResponse('Bienvenido a la api')