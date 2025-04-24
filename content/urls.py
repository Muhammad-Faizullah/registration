from django.urls import path
from .views import ProductApi,ProductApi_2

urlpatterns = [
    path('ListOfProducts/',ProductApi.as_view()),
    path('CreationOfProduct/',ProductApi.as_view()),
    path('ChangesInProduct/<int:pk>/',ProductApi_2.as_view()),
    path('DeletionOfProduct/<int:pk>/',ProductApi_2.as_view()),

]