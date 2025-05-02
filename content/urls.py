from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ProductListView,ProductRetrieveView,CategoryListView,CategoryRetrieveView,ProductCreateView,ProductRUDView

urlpatterns = [
    path('Product/List/',ProductListView.as_view()),
    path('Product/Retrieve/<int:pk>/',ProductRetrieveView.as_view()),
    path('CreationOfProduct/',ProductCreateView.as_view()),
    path('ChangesInProduct/<int:pk>/',ProductRUDView.as_view()),
    path('DeletionOfProduct/<int:pk>/',ProductRUDView.as_view()),
    path('Category/list/',CategoryListView.as_view()),
    path('Category/Create/',CategoryListView.as_view()),
    path('Category/Change/<int:pk>/',CategoryRetrieveView.as_view()),
    path('Category/Delete/<int:pk>/',CategoryRetrieveView.as_view())
    
] 
