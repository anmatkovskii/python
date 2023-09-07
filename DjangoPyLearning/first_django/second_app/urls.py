from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main_page),
    path('main/', views.main_page, name='main'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('news/', views.news, name='news'),
    path('rulers/', views.rulers, name='rulers'),
    path('dictsort/', views.dictsort, name='dictsort'),
    path('dbshow/', views.dbshow, name='dbshow'),
    path('product/', views.product, name='product')
]

