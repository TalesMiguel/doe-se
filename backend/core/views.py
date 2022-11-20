import json

from django.http import HttpResponse, JsonResponse
from django.contrib import auth

def hello(request):
    return HttpResponse("Hello, World!")