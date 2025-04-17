from django.shortcuts import render
from .models import User
from .serializer import RegisterSerializer,LoginSerializer
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView,RetrieveAPIView
from rest_framework.permissions import IsAdminUser
# Create your views here.


class RegisterApi(ListAPIView,CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    # permission_classes = [IsAdminUser]
    
class LoginApi(CreateAPIView):
    # queryset = User.objects.all()
    serializer_class = LoginSerializer