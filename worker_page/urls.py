from django.contrib import admin
from django.urls import path , include
from worker_page import views

urlpatterns = [
    path('/login', views.login, name="login"),
    path('/list', views.list, name="list"),
]