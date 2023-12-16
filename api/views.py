from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView



# Create your views here.
def api_index(request):
    return HttpResponse("Hello World")
