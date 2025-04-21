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
    otp = serializers.CharField(max_length=4,read_only=True)
    
    def validate(self, attrs):
        email = attrs.get('email')
        try:
            user_obj = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError({"error":"invalid email"})

        digits = '256789'
        # print('otp',digits[math.floor(random.random() * 10)])
        otp = digits[math.floor(random.random() * 10)]
        Otp.objects.create(user = user_obj, otp=otp)
        return attrs

