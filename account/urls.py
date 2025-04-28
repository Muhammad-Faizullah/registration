from django.contrib import admin
from django.urls import path
from .views import RegisterApi,LoginApi,ChangePasswordApi,ResetPasswordApi,GenerateOTPApi,UserProfileApi,UploadFileApi

urlpatterns = [
    path('register/',RegisterApi.as_view()),
    path('login/',LoginApi.as_view()),
    path('changePassword/',ChangePasswordApi.as_view()),
    path('resetPassword/',ResetPasswordApi.as_view()),
    path('generateOtp/',GenerateOTPApi.as_view()),
    path('profile/',UserProfileApi.as_view()),
    path('uploadFile/',UploadFileApi.as_view())
]