from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.mpesa_index, name='mpesa_index'),
    path('mpesa_payment/', views.mpesa_payment, name='mpesa_payment'),
]