from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main_page),
    path('fruits/', views.get_fruits, name='fruits'),
    path('vegetables/', views.get_vegetables, name='vegetables')
]