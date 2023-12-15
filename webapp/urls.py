from django.urls import path
from . import views 

urlpatterns = [
    path('', views.register, name='register'),
    path('index/', views.webapp_index, name="webapp_index")
    
]