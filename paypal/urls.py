from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.paypal_index, name='paypal_index')
]