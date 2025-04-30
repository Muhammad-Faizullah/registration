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

class CategoryListView(ListAPIView,CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [JWTAuthentication]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset = CategoryFilter
    
class CategoryRetrieveView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [JWTAuthentication]

class ProductListView(APIView):
    # authentication_classes = [JWTAuthentication]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fileds = ['name','category']
    
    def get(self,request,*args,**kwargs):
        id = kwargs.get('pk')
        print(id)
        
        if id is None:
            print('---------')
            obj = Product.objects.all()
            serializer = ProductListSerializer(obj,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        
        try:
            obj = Product.objects.get(id=id)
            serializer = ProductListSerializer(obj)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({"error":"This product does not exist"})

class ProductCreateView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self,request,*args,**kwargs):
        user = self.request.user
        print(user)
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ProductRetrieveView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    