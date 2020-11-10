from todo.core.base.models import Todo
from todo.core.base.models import User

from rest_framework import serializers


class TodoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Todo
        fields = ['uuid', 'value', 'checked', 'owner']


class UserSerializer(serializers.ModelSerializer):
    todos = serializers.PrimaryKeyRelatedField(many=True, queryset=Todo.objects.all())

    class Meta:
        model = User
        fields = ['uuid', 'username', 'todos']
