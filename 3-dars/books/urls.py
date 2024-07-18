from django.urls import path
from .views import BookListApiView, book_list_view, BookDetailView

urlpatterns = [
    path('', BookListApiView.as_view(), ),
    path('<int:pk>/', BookDetailView.as_view()),
    path('books/', book_list_view),
]
