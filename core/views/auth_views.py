
from rest_framework.response import Response
from rest_framework import generics, permissions
from rest_framework.decorators import api_view, permission_classes
from ..serializers import RegisterSerializer
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework.permissions import AllowAny

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]