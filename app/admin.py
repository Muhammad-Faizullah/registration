from django.contrib import admin
from .models import User,Otp
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','username','email','password']
    
@admin.register(Otp)
class OtpAdmin(admin.ModelAdmin):
    list_display = ['id','user','otp']