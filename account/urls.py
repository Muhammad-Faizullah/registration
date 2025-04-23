from django.contrib import admin
from django.urls import path
from .views import RegisterApi,LoginApi,ChangePasswordApi,ResetPasswordApi,GenerateOTPApi,UserProfileApi

urlpatterns = [
    path('account/register/',RegisterApi.as_view()),
    path('account/login/',LoginApi.as_view()),
    path('account/changePassword/',ChangePasswordApi.as_view()),
    path('account/resetPassword/',ResetPasswordApi.as_view()),
    path('account/generateOtp/',GenerateOTPApi.as_view()),
    path('account/profile/',UserProfileApi.as_view())
]