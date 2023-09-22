from django.contrib import admin
from django.urls import path , include
from manager_page import views

urlpatterns = [
    path('', views.admin_login, name="admin_login"),
    path('adminlogin',views.admin_login , name="adminlogin"),
    path('add',views.add_emp , name='add'),
    path('dash', views.dash , name="dash"),
    path('add_emp' , views.add_emp, name='add_emp'),
    path('upload',views.upload, name="upload"),
]