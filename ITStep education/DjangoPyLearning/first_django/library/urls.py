from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main_page_library),
    path('main/', views.main_page_library, name='main'),

]