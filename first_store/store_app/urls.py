from django.contrib import admin
from django.urls import path, include
from store_app import views

urlpatterns = [

    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
     path('register/', views.register, name='register'),
]