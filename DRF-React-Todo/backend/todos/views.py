from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import *
from .serializers import TodoSerializers


# Create your views here.

class ListTodos(ListAPIView):
    queryset = Todos.objects.all()
    serializer_class = TodoSerializers
class DetailTodo(RetrieveAPIView):
    queryset = Todos.objects.all()
    serializer_class = TodoSerializers