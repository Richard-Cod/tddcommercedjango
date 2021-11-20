
# Create your views here.

from core.models import User
from .serializers import UserSerializer

from rest_framework.permissions import AllowAny

from rest_framework import viewsets


# Create your views here.

# ViewSets define the view behavior.
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [AllowAny]
