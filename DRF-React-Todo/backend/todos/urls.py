from django.urls import path
from .views import ListTodos, DetailTodo

urlpatterns = [
    path('<int:pk>', DetailTodo.as_view()),
    path('', ListTodos.as_view())
]