
from django.shortcuts import render
from content.models import Product
from .models import Order
from .serializer import OrderSerializer,OrderListSerializer,PaymentSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView,RetrieveAPIView
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
from django.core.files.storage import Storage,default_storage,DefaultStorage
from content.filters import CategoryFilter,ProductFilter
from django_filters import rest_framework as filters
from account.permissions import AdminPermission,OwnerPermission
from rest_framework import viewsets

# Create your views here.

class OrderView(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def order_product(self,request):
        serializer = OrderSerializer(data=request.data,context={"request":request})
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
 
class OrderListView(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AdminPermission] 

    def order_list(self,request):
        obj = Order.objects.all()
        serializer = OrderListSerializer(obj,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)   
    
class PaymentView(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def payment(self,request):
        serializer = PaymentSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)