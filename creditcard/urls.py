from django.urls import path
from . import views 

urlpatterns = [
    path('', views.credit_card_payment, name='credit_card_payment'),
]