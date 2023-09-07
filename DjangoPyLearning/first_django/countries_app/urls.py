from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('', views.main),
    path('main/', views.main, name='main'),
    path('history/', views.history, name='history'),
    re_path(r'^history/(?P<year>[0-9]{1,4})/$', views.history_year, name='history_year'),
    path('cities/', views.cities, name='cities'),
    path('facts/', views.facts, name='facts'),
    re_path(r'^cities/(?P<city_name>\w+)/$', views.city, name='city'),
    re_path(r'^cities/(?P<city_name>\w+)/(?P<year>[0-9]{1,4})/$', views.city_year, name='city_year')
]