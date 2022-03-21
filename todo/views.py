from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer
from .permissions import IsCreatorOrReadOnly


class TodoList(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsCreatorOrReadOnly, )
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
