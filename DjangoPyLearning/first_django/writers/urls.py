from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.main_page),
    path('main/', views.main_page, name='main'),
    path('writers/', views.writers, name='writers'),
    path('top_books/', views.top_books, name='top_books'),
    re_path(r'^writers/(?P<name>[A-Za-z]{1,})/$', views.writer_by_name, name='writer_name'),
    re_path(r'^top_books/(?P<book>[0-9]{1,})/$', views.book_by_number, name='book_by_number'),
    re_path(r'^writers/(?P<name>[A-Za-z]{1,})/(?P<book>[ A-Za-z0-9:,?-]{1,})/$', views.book_by_name_author,
            name='book_by_name_author'),
    re_path(r'^writers/writer=(?P<name>[A-Za-z]{1,}) year=(?P<year>[0-9]{4})/$', views.book_by_year, name='book_by_year'),
]