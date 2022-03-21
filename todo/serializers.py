from dataclasses import fields
import imp
from pyexpat import model
from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = (
            'id',
            'title',
            'description',
            'created_at',
            'deadline',
            'creator',
            'status',
        )
        