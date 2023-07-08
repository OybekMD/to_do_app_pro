from rest_framework import serializers
from .models import ToDoListModel

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoListModel
        fields = '__all__' 