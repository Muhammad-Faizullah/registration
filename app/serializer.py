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

    