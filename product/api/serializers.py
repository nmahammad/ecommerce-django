from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from product.models import Category, Product, Brand


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = (
            'id',
            'title',
            'created_at',
            'updated_at',
        )


class CategoryCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = (
        'id',
        'title',
        'parent_id',
    )

    def get_parent_id(self, obj):
        if obj.parent_id:
            return obj.parent_id.title
        return "No parent"



class CategoryReadSerializer(serializers.ModelSerializer):
    parent_id = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = (
        'id',
        'title',
        'parent_id',
    )

    def get_parent_id(self, obj):
        if obj.parent_id:
            return obj.parent_id.title
        return "No parent"




class BrandSerializer(serializers.ModelSerializer):
    class Meta :
        model = Brand 
        fields = [
            'id',
            'title',
        ]
        

class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ( 
            'category_id',
            'vendor_id',
            'brand_id',
            'title',
            'description',
        )

class ProductReadSerializer(serializers.ModelSerializer):
    category_id = CategorySerializer()
    brand_id = BrandSerializer()
    
    class Meta:

        model = Product
        fields = ( 
            'category_id',
            'vendor_id',
            'brand_id',
            'title',
            'description',
        )

