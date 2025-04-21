from django.shortcuts import render
from .models import User,Otp
from .serializer import RegisterSerializer,LoginSerializer,ChangePasswordSerializer,ResetPasswordSerializer,GenerateOtpSerializer
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView,RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
import math,random
# Create your views here.

# def generate_token(user):
#     refresh_token = RefreshToken.for_user(user)
#     return {
#         "refresh token":str(refresh_token),
#         "access token":str(refresh_token.access_token)
#     }

class RegisterApi(ListAPIView,CreateAPIView ):
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
            return Response(serializer.errors,status=status.HTTP_401_UNAUTHORIZED)
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
            return Response(serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)

class ResetPasswordApi(APIView):
    
    def post(self,request,*args,**kwargs):
        serializer = ResetPasswordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_401_UNAUTHORIZED)
                
class GenerateOTPApi(APIView):
    # authentication_classes = []
    # permission_classes = []
    
    def get(self,request,*args,**kwargs):
        obj = Otp.objects.all()
        serializer = GenerateOtpSerializer(obj,many=True)
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
    
    def post(self,request,*args,**kwargs):
        serializer = GenerateOtpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_401_UNAUTHORIZED)
