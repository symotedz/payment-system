from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def paypal_index(request):
    return HttpResponse("Hello PayPal Index")
