from django.shortcuts import render
from .models import Product
from .serializer import ProductSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class ProductApi(APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    
    def get(self,request,*args,**kwargs):
        obj = Product.objects.all()
        serializer = ProductSerializer(obj,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request,*args,**kwargs):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,*args,**kwargs):
        id = self.kwargs.get('pk')
        if id is None:
            return Response({'error':'provide id of the product you want to update'})
        obj = Product.objects.get(id=id)
        serializer = ProductSerializer(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,*args,**kwargs):
        print('kwargs',self.kwargs)
        id = self.kwargs.get('pk')
        if id is None:
            return Response({'error':'provide id of the product you want to update'})
        obj = Product.objects.get(id=id)
        serializer = ProductSerializer(obj,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,*args,**kwargs):
        id = self.kwargs.get('pk')
        obj = Product.objects.get(id=id)
        print('obj',obj)
        obj.delete()
        print('obj',obj)
        return Response({"message":"object deleted"},status=status.HTTP_404_NOT_FOUND)
        