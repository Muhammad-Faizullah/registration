from django.shortcuts import render
from .models import User
from .serializer import RegisterSerializer,LoginSerializer,ChangePasswordSerializer,ResetPasswordSerializer
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView,RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken,AccessToken
# Create your views here.


class RegisterApi(ListAPIView,CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    
class LoginApi(APIView):
    
    def post(self,request,*args,**kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            print(email,password)
            if email and password is not None:
                user = authenticate(email=email,password=password)
                print('user',user)
                if user is not None:
                    return Response('Login successful')

class ChangePasswordApi(APIView):
    
    def post(self,request,*args,**kwargs):
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.data.get('old_password'))
            print(serializer.data.get('new_password'))
            email = serializer.data.get('email')
            old_password = serializer.validated_data.get('old_password')
            new_password = serializer.validated_data.get('new_password')
            user = authenticate(email=email,password=old_password)
            if user is not None:
                print('user',user)
                print(User.objects.get(email=email))
                user_obj = User.objects.get(email=email)
                if user_obj is not None:
                    print('user_obj',user_obj)
                    print(user_obj.password)
                    # user_obj.password = new_password
                    # print(user_obj.password)
                    user_obj.set_password(new_password)
                    print(user_obj.password)
                    user_obj.save()
                    
                    return Response('Password Changed')

class ResetPasswordApi(APIView):
    
    def post(self,request,*args,**kwargs):
        serializer = ResetPasswordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
                