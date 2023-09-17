from django.contrib import admin
from django.urls import path , include
from manager_page import views

urlpatterns = [
    path('', views.dash, name="dash"),
    path('adminlogin',views.admin_login , name="adminlogin"),
    path('add',views.add_emp , name='add')
]