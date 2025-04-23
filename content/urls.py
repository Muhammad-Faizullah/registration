from django.urls import path
from .views import ProductApi

urlpatterns = [
    path('getAll/',ProductApi.as_view()),
    path('get/<int:pk>/',ProductApi.as_view()),
    path('create/',ProductApi.as_view()),
    path('fullUpdate/<int:pk>/',ProductApi.as_view()),
    path('partialUpdate/<int:pk>/',ProductApi.as_view()),
    path('Delete/<int:pk>/',ProductApi.as_view)
]
