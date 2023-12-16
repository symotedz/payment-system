from django.urls import path
from . import views 

urlpatterns = [
    path('', views.user_login, name="user_login"),
    path('register/', views.register, name='register'),
    path('webapp_index/', views.webapp_index, name="webapp_index"),
]