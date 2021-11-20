from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from .models import Customer
from core.models import User

from core.serializers import UserSerializer


class SimpleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username']


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    user = SimpleUserSerializer()

    class Meta:
        model = Customer
        fields = ["user", "subscription"]
