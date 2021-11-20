from django.shortcuts import get_object_or_404

from .models import Customer
from core.models import User
from .serializers import CustomerSerializer

from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from rest_framework import viewsets

from rest_framework.response import Response
from rest_framework.decorators import action


# Create your views here.

# ViewSets define the view behavior.


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    @action(detail=False, methods=['get'], name='Current Customer')
    def me(self, request, pk=None):
        c = self.request.user.customer
        serializer = self.get_serializer(c)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        print(self.request.user)
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_permissions(self):
        if self.action == 'me':
            return [IsAuthenticated()]

        return [IsAuthenticatedOrReadOnly()]

    # def get_permissions(self):
    #     if self.request.method == 'POST':
    #         return Au
    #     print(self.request.method)
    #     print("putain de border")
