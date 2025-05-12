from django.shortcuts import render
from .models import Product,ProductImage,Category
from .serializer import ProductSerializer,CategorySerializer,ProductListSerializer
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


class PublishingView(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AdminPermission]
        
    def product_publish(self,request,pk):

        try:    
            id = pk
            obj = Product.objects.get(id=id)
            if obj.publish == True:
                return Response({"message":"this product is already published"},status=status.HTTP_400_BAD_REQUEST)
            obj.publish = True
            obj.save()
        except Product.DoesNotExist:
            return Response({"error":"valid id is required"})
        return Response({"message":"product published"},status=status.HTTP_201_CREATED)
    
    def product_unpublish(self,request,pk):

        try:
            id = pk
            obj = Product.objects.get(id=id)
            if obj.publish == False:
                return Response({"message":"this product is already unpublished"},status=status.HTTP_400_BAD_REQUEST)
            obj.publish = False
            obj.save()        
        except Product.DoesNotExist:
            return Response({"error":"valid id is required"})
        return Response({"message":"product unpublished"},status=status.HTTP_201_CREATED)


class CategoryListView(ListAPIView,CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [OwnerPermission,AdminPermission]
    filter_backends = (filters.DjangoFilterBackend)
    filterset_class = CategoryFilter 
class CategoryRetrieveView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [OwnerPermission,AdminPermission]
    

class ProductListView(ListAPIView):
    queryset = Product.objects.filter(publish=True)
    serializer_class = ProductListSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = ProductFilter   
class ProductRetrieveView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
        

class AdminProductListView(ListAPIView):
    queryset = Product.objects.order_by('id').reverse()
    serializer_class = ProductListSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class AdminProductCreateView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AdminPermission]
    
    def post(self,request,*args,**kwargs):
        user = self.request.user
        print(user)
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class AdminProductRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [AdminPermission]
    

        