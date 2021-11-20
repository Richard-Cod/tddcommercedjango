from rest_framework import serializers
from .models import User
from store.models import Customer
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
# Serializers define the API representation.
from django.db import transaction


class UserCreateSerializer(BaseUserCreateSerializer):
    def create(self, validated_data):
        try:
            with transaction.atomic():
                user = self.perform_create(validated_data)
                Customer(user=user).save()
                return user
        except IntegrityError:
            self.fail("cannot_create_user")


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
