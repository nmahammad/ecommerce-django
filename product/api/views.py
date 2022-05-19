from itertools import product
from rest_framework.views import APIView
from rest_framework.response import Response

from product.api.serializer import ProductSerializer
from product.models import Product, Review


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
