from django.shortcuts import render
from .models import User
from .serializer import RegisterSerializer
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView,RetrieveAPIView
# Create your views here.


class RegisterCreateApi(CreateAPIView):
    serializer_class = RegisterSerializer

class RegisterListApi(ListAPIView):
    queryset = User.objects.all()