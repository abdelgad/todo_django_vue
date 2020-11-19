from django.shortcuts import render

from todo.core.base.models import Todo
from todo.core.base.models import User

from .serializers import TodoSerializer
from .serializers import UserSerializer
from .permissions import IsOwnerOrRefuse

from rest_framework import generics
from rest_framework import permissions
from rest_framework.exceptions import ValidationError


class TodoList(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(owner=user)

    def perform_create(self, serializer):
        if(Todo.objects.filter(value=self.request.data['value'], owner=self.request.user)):
            raise ValidationError('You have already added that todo')

        serializer.save(owner=self.request.user)


class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [IsOwnerOrRefuse]
    lookup_field = 'uuid'


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
