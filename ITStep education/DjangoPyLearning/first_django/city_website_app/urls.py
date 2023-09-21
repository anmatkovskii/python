from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('', views.main),
    path('main/', views.main, name='city_main'),
    path('news/', views.news, name='city_news'),
    path('city_heads/', views.city_heads, name='city_heads'),
    path('facts/', views.facts, name='city_facts'),
    path('contacts/', views.contacts, name='city_contacts'),
    path('history/', views.history_main, name='city_history'),
    path('history/photo', views.history_photos, name='city_history_1'),
    path('history/people', views.history_people, name='city_history_2')
]