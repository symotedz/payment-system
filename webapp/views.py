from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def webapp_index(request):
    return HttpResponse("Hello WebApp Index")
