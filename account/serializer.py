from rest_framework import serializers
from rest_framework.serializers import ValidationError
from .models import User,Otp
from rest_framework.response import Response
from rest_framework.authentication import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
import math,random


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=50)

    def validate(self,attrs):
        email = attrs.get('email')

        if email == "" :
            raise ValidationError({"error":"valid email is required"})
        
        user_obj = User.objects.filter(email=email)

        if user_obj.exists():
            raise ValidationError({"message":"User with this email is already registered"})

        return attrs
    
    def create(self, validated_data):
        return User.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
            password = validated_data['password']
        )
        
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=50)
                      
    def validate(self,attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email is None:
            raise serializers.ValidationError({"email":"must not be empty"})
        
        if password is None:
            raise serializers.ValidationError({"password ":"must not be empty"})

        return attrs


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=50)
    new_password = serializers.CharField(max_length=50)
    confirm_new_password = serializers.CharField(max_length=50)
    
    def validate(self,attrs):
        old_password = attrs.get('old_password')
        new_password = attrs.get('new_password')
        confirm_new_password = attrs.get('confirm_new_password')
        request = self.context.get('request')
        user_obj = request.user

        if user_obj is None:
            raise ValidationError({"message":"Invalid"})
                    
        if old_password is None:
            raise ValidationError({"old_password":"this field should not be empty"})
        
        if new_password is None:
            raise ValidationError({"new_password":"should not be empty"})
        
        if old_password is None:
            raise ValidationError({"old_password":"should not be empty"})
        
        if old_password == new_password:
            raise ValidationError({"message":"old and new password should not match"})
        
        if new_password != confirm_new_password:
            raise ValidationError({"message":"new and confirm password should match"})

        user_obj_password = user_obj.check_password(old_password)

        if user_obj_password is False:
            raise ValidationError({"old_password":"Invalid password"})

        user_obj.set_password(new_password)
        user_obj.save()
        return attrs

class ResetPasswordSerializer(serializers.Serializer):
    otp = serializers.CharField(max_length=4,write_only=True)
    password = serializers.CharField(max_length=50)

    def validate(self,attrs):
        otp = attrs.get('otp')
        
        try:
            otp_obj = Otp.objects.get(otp=otp)
            user_obj = otp_obj.user
        except Otp.DoesNotExist:
            raise serializers.ValidationError({"error":"Invalid Otp"})
        
        password = attrs.get('password')
        user_obj_password = user_obj.check_password(password)   
        
        if user_obj_password is True:
            raise serializers.ValidationError({"message":"password is similar to old password"})

        user_obj.set_password(password)
        user_obj.save()
        Otp.objects.filter(id=otp_obj.id).delete()
        return attrs

class GenerateOtpSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)
    otp = serializers.CharField(max_length=4,read_only=True)
    
    def validate(self, attrs):
        email = attrs.get('email')
        
        try:
            user_obj = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError({"error":"invalid email"})

        otp = random. randint(1000, 9999)
        attrs['user'] = user_obj
        attrs['otp'] = otp
        return attrs

    def create(self,validated_data):
        validated_data.pop('email')
        return Otp.objects.create(**validated_data)

       
class UserProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id','email','date_of_birth','phone_number','country','state','city']
        read_only_fields = ['id','email']
    
    