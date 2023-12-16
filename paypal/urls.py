from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.paypal_payment, name='paypal_payment'),
]