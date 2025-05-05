from django.shortcuts import render
from .models import User,Otp
from .serializer import RegisterSerializer,LoginSerializer,ChangePasswordSerializer,ResetPasswordSerializer,GenerateOtpSerializer,UserProfileSerializer,AdminUserSerializer
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView,RetrieveAPIView
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
import math,random
from rest_framework.serializers import ValidationError
from django.core.files.storage import Storage,default_storage,DefaultStorage
from .permissions import OwnerPermission

class AdminUserView(ListAPIView,CreateAPIView):
    queryset = User.objects.all()
    serializer_class = AdminUserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [OwnerPermission]

class AdminUserRUDView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = AdminUserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [OwnerPermission]
    
    

class RegisterView(APIView):

    def post(self,request,*args,**kwargs):
        serializer = RegisterSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"user registered successfully"},status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(APIView):
    
    def post(self,request,*args,**kwargs):
        serializer = LoginSerializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.data.get('user_detail')
            token = serializer.data.get('token_detail')
            return Response({"User":user,"Token":token},status=status.HTTP_200_OK)    
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ChangePasswordView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self,request,*args,**kwargs):
        serializer = ChangePasswordSerializer(data=request.data,context={"request":request})
        
        if serializer.is_valid():
            return Response({"message":"password changed successfully"},status=status.HTTP_200_OK)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ResetPasswordView(APIView):
    
    def post(self,request,*args,**kwargs):
        serializer = ResetPasswordSerializer(data=request.data)
        
        if serializer.is_valid():
            return Response({"message":"password reset successfully"},status=status.HTTP_200_OK)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
                
class GenerateOTPView(APIView):
    
    def post(self,request,*args,**kwargs):
        serializer = GenerateOtpSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UserProfileView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self,request,*args,**kwargs):
        user = request.user
        serializer = UserProfileSerializer(user)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,*args,**kwargs):
        user = request.user
        serializer = UserProfileSerializer(user,data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UploadFileView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self,request,*args,**kwargs):
        folder = request.data.get('folder')
        file = request.data.get('file')
        
        if folder is None:
            return Response({"error":"folder is required"},status=status.HTTP_400_BAD_REQUEST)
        
        if file is None:
            return Response({"error":"file is required"},status=status.HTTP_400_BAD_REQUEST)
        
        full_path = f'{folder}/{file.name}'        
        saved_file = default_storage.save(full_path,file)
        file_url = default_storage.url(saved_file)
        return Response({"url":file_url,"path":str(full_path)})