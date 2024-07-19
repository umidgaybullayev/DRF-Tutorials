from django.urls import path
from .views import *

urlpatterns = [
    path('books/', BookListApiView.as_view(), ),
    path('book/', BookListCreateApiView.as_view()),
    path('books/create/', BookCreateApiView.as_view()),
    path('books/<int:pk>/', BookDetailAPIView.as_view()),
    path('books/<int:pk>/delete/', BookDeleteAPIView.as_view()),
    path('books/<int:pk>/update/', BookUpdateAPIView.as_view()),
    # path('books/', book_list_view),
]
