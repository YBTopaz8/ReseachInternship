from django.contrib.auth import login
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home , name="home"),
    path('login/', views.login_user, name="login"),
    path('code_val/', views.code_val, name="code_valid"),
]
