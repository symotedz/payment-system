from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def credit_card_index(request):
    return HttpResponse("Hello credit Card")


def credit_card_payment(request):
    return render(request, "credit_card.html")
