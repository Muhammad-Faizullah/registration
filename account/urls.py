from django.contrib import admin
from django.urls import path
from .views import RegisterView,LoginView,ChangePasswordView,ResetPasswordView,GenerateOTPView,UserProfileView,UploadFileView,AdminUserRUDView,AdminUserView

urlpatterns = [
    path('register/',RegisterView.as_view()),
    path('login/',LoginView.as_view()),
    path('changePassword/',ChangePasswordView.as_view()),
    path('resetPassword/',ResetPasswordView.as_view()),
    path('generateOtp/',GenerateOTPView.as_view()),
    path('profile/',UserProfileView.as_view()),
    path('uploadFile/',UploadFileView.as_view()),
    path('user/',AdminUserView.as_view()),
    path('user/create/',AdminUserView.as_view()),
    path('user/change/<int:pk>/',AdminUserRUDView.as_view()),
    path('user/delete/<int:pk>/',AdminUserRUDView.as_view())
]