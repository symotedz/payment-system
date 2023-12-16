from django.urls import path 
from . import views 

urlpatterns = [
    path('mpesa_payment/', views.mpesa_payment, name='mpesa_payment'),
]