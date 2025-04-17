from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.Serializer):
    GENDER = [
        (MALE,"male"),
        (FEMALE,"female"),
        (CUSTOM,"custom")
    ]
    
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    birthday = serializers.DateField()
    gender = serializers.CharField(max_length=25,choices=GENDER)
    email = serializers.EmailField(unique=True)
    password = serializers.CharField(max_length=50)
    