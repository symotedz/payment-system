from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.paypal_index, name='paypal_index'),
    path('paypal_payment/', views.paypal_payment, name='paypal_payment'),
]