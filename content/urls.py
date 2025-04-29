from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ProductApi,ProductApi_2,CategoryApi,CategoryApi_2,CategoryApi_3

urlpatterns = [
    path('ListOfProducts/',ProductApi.as_view()),
    path('CreationOfProduct/',ProductApi.as_view()),
    path('ChangesInProduct/<int:pk>/',ProductApi_2.as_view()),
    path('DeletionOfProduct/<int:pk>/',ProductApi_2.as_view()),
    path('Category/list/',CategoryApi.as_view()),
    path('Category/Create/',CategoryApi_2.as_view()),
    path('Category/Change/<int:pk>/',CategoryApi_3.as_view()),
    path('Category/Delete/<int:pk>/',CategoryApi_3.as_view())
    
] 
