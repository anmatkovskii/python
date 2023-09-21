from django.urls import path, include
from . import views
from main_backend.views import TasksAPIView, UsersAPIView, TaskUpdateAPIView

urlpatterns = [
    path('tasks/', TasksAPIView.as_view()),
    path('users/', UsersAPIView.as_view()),
    path('tasks/<int:pk>/', TaskUpdateAPIView.as_view()),
]