from rest_framework import serializers
from .models import User
from rest_framework.response import Response
from rest_framework.authentication import authenticate

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
    
    def validate(self,data):
        email = data.get('email')
        password = data.get('password')
        
        if email and password:
            obj = authenticate(email=email,password=password)
            return obj
        return data

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=50)
    new_password = serializers.CharField(max_length=50)
    confirm_new_password = serializers.CharField(max_length=50)
    
    def validate(self,data):
        if data['old_password'] == data['new_password']:
            raise serializers.ValidationError("old and new password cannot be same")
        if data['new_password'] != data['confirm_new_password']:
            raise serializers.ValidationError("confirm_new_password and new_password are not similar")
        