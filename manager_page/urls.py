from django.contrib import admin
from django.urls import path , include
from manager_page import views

urlpatterns = [
    path('', views.dash, name="dash"),
]