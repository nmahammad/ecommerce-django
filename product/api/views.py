from itertools import product
from rest_framework.views import APIView
from rest_framework.response import Response

from product.api.serializer import ProductSerializer
from product.models import Product, Review
from drf_yasg.utils import swagger_auto_schema


        
from functools import partial
from multiprocessing import context
from unicodedata import category
from rest_framework.status import (
  HTTP_200_OK,
  HTTP_201_CREATED,
  HTTP_204_NO_CONTENT,
  )
from django.http import Http404

from product.api.serializers import CategoryReadSerializer, CategoryCreateSerializer
from product.models import Category



class ReviewAPI(APIView):

    
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = ProductSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=201) 


class ProductAPI(APIView):

    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        serializer = ProductSerializer(
            products, many=True, context={'request': request})
        return Response(data=serializer.data)






class CategoryAPI(APIView):

 def get(self,request,*args, **kwargs):
  """
    This endpoint for get all categories
  """
  categories = Category.objects.all()
  parent = request.GET.get('parent')
  if parent:
    categories = Category.objects.filter(parent_id=parent)
  serializer = CategoryReadSerializer(categories, many=True, context={'request': request})
  return Response(data=serializer.data)

 
 @swagger_auto_schema(query_serializer=CategoryCreateSerializer, request_body=CategoryCreateSerializer)
 def post(self,request,*args, **kwargs):
  """
    This endpoint for creat new categorie
  """
  data = request.data
  print(data)
  serializer = CategoryCreateSerializer(data=data)
  serializer.is_valid(raise_exception=True)
  serializer.save()
  return Response(data=serializer.data, status=HTTP_201_CREATED) 



class CategoryDetailAPI(APIView):

 def get(self,request,*args, **kwargs):
  """
    This endpoint for detail categorie
  """
  category = Category.objects.filter(id=kwargs['pk']).first()
  if not category:
   raise Http404
  serializer = CategoryReadSerializer(category, context={'request': request})
  return Response(data=serializer.data)
  
 @swagger_auto_schema(query_serializer=CategoryCreateSerializer, request_body=CategoryCreateSerializer)
 def put(self,request,*args, **kwargs):
  """
    This endpoint for to update all items categorie
  """
  category = Category.objects.filter(id=kwargs['pk']).first()
  if not category:
    raise Http404
  serializer = CategoryCreateSerializer(data=request.data, instance=category)
  serializer.is_valid(raise_exception=True)
  serializer.save()
  return Response(data=serializer.data, status=HTTP_200_OK)

 @swagger_auto_schema(query_serializer=CategoryCreateSerializer, request_body=CategoryCreateSerializer)
 def patch(self,request,*args, **kwargs):
  """
    This endpoint for to update only one item categorie
  """
  category = Category.objects.filter(id=kwargs['pk']).first()
  if not category:
    raise Http404
  serializer = CategoryCreateSerializer(data=request.data, partial=True, instance=category)
  serializer.is_valid(raise_exception=True)
  serializer.save()
  return Response(data=serializer.data, status=HTTP_200_OK) 


 def delete(self,request,*args, **kwargs):
  """
    This endpoint for delet categorie
  """
  delete_category, _ = Category.objects.filter(id=kwargs['pk']).delete()
  print(delete_category, _)
  if delete_category == 0:
    raise Http404
  return Response(data={}, status=HTTP_204_NO_CONTENT) 
