# from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse
# from .models import Todo

# # Create your views here.

# def index(req):
#     todo = Todo.objects.all()
#     data = {'key':'value'}
#     # return HttpResponse("<h1>Data</h1>", content_type='text/plain')
#     return JsonResponse(data, safe=False)
# ______________

from rest_framework import generics

from .models import *
from .serializers import TodoSerializer

class ListTodo(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer