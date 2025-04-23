from django.shortcuts import render
from .models import User,Otp
from .serializer import RegisterSerializer,LoginSerializer,ChangePasswordSerializer,ResetPasswordSerializer,GenerateOtpSerializer,UserProfileSerializer
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


class RegisterApi(APIView):

    def post(self,request,*args,**kwargs):
        serializer = RegisterSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"user registered successfully"},status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class LoginApi(APIView):
    
    def post(self,request,*args,**kwargs):
        serializer = LoginSerializer(data=request.data)
        
        if serializer.is_valid():
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email,password=password)
            
            if user is None:
                raise ValidationError({"error":"Invalid credentials"})
            
            username = user.username
            email = user.email
            refresh_token = RefreshToken.for_user(user)
            access_token = str(refresh_token.access_token)
            return Response({"message":"login successful","user":{"id":user.id,"username":username,"email":email},"tokens":{"refresh_token":str(refresh_token),"access_token":access_token}},status=status.HTTP_200_OK)    
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ChangePasswordApi(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self,request,*args,**kwargs):
        serializer = ChangePasswordSerializer(data=request.data,context={"request":request})
        
        if serializer.is_valid():
            return Response({"message":"password changed successfully"},status=status.HTTP_200_OK)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ResetPasswordApi(APIView):
    
    def post(self,request,*args,**kwargs):
        serializer = ResetPasswordSerializer(data=request.data)
        
        if serializer.is_valid():
            return Response({"message":"password reset successfully"},status=status.HTTP_200_OK)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
                
class GenerateOTPApi(APIView):
    
    def post(self,request,*args,**kwargs):
        serializer = GenerateOtpSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UserProfileApi(APIView):
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
