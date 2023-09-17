from django.contrib import admin
from django.urls import path , include
from worker_page import views

urlpatterns = [
    path('/login', views.emp_login, name="login"),
    path('/emp_dash',views.emp_dash , name="emp_dash"),
]