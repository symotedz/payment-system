from django.urls import path
from . import views 

urlpatterns = [
    path('', views.webapp_index, name="webapp_index")
]