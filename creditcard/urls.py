from django.urls import path
from . import views 

urlpatterns = [
    path('', views.credit_card_index, name='credit_card_index'),
    path('credit_card/', views.credit_card_payment, name='credit_card_payment'),
]