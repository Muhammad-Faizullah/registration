from django.contrib import admin
from .models import User,Otp
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','username','email','is_active']
    search_fields = ['username','email']
    list_filter = ['is_active','is_admin']
    list_per_page = 15
    
@admin.register(Otp)
class OtpAdmin(admin.ModelAdmin):
    list_display = ['id','user','otp']
    list_filter = ['user']
