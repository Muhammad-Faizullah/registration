from rest_framework import serializers
from .models import User,Otp
from rest_framework.response import Response
from rest_framework.authentication import authenticate
import math,random
class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return User.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
            password = validated_data['password']
        )
        
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=50)
                      

class ChangePasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    old_password = serializers.CharField(max_length=50)
    new_password = serializers.CharField(max_length=50)
    confirm_new_password = serializers.CharField(max_length=50)
    

class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate(self,data):
        pass

class GenerateOtpSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=100)
    otp = serializers.CharField(max_length=4,read_only=True)
    
    # def otp_generator(user):
    #     digits = '0123456789'
    #     otp = ''
    #     for i in range(4):
    #         otp += digits[math.floor(random.random() * 10)]
    #         print('otp',otp)
    #         return otp
    
    def validate(self, data):
        email = data.get('email')
        print('email',email)
        username = data.get('username')
        print('username',username)
        user = authenticate(username=username,email=email)
        print('user',user)
        if user:
            digits = '0123456789'
            otp = ''
            for i in range(4):
                otp += digits[math.floor(random.random() * 10)]
                return otp
            
                
        return data
    
    def create(self,validated_data):
        return Otp.objects.create(
            email = validated_data['email'],
            otp = validated_data['otp_for']['otp']
        )   

