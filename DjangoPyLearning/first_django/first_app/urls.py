from django.urls import path, include, re_path
from first_app.views import add, show_info, phone_valid, gmail_valid

urlpatterns = [
    path('add/<str:product_name> <int:price>/', add),
    path('show/<str:product_name>/', show_info),
    re_path(r'^phone/(?P<phone>\+[\d]{12})$', phone_valid),
    re_path(r'^gmail/(?P<gmail>[A-Za-z0-9_.]{1,}(@gmail\.com))$', gmail_valid)
]
