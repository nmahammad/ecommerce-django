from rest_framework import serializers
from product.models import Product , Category

class ProductSerializer(serializers.ModelSerializer):

    category = serializers.CharField(source = 'category.title')

    class Meta:
        model = Product
        fields = (
            'id', 
            'title',
        )


# class TagSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tag
#         fields = (
#             'id',
#             'title'
#         )


# class StoryCreateSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Story
#         fields = (
#             'category',
#             'author',
#             'tags',
#             'title',
#             'slug',
#             'image',
#             'cover_image',
#             'content',
#             'created_at',
#             'updated_at',
#         )




# class StoryReadSerializer(serializers.ModelSerializer):
#     category = CategorySerializer()
#     tags = TagSerializer(many=True)
#     # created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

#     class Meta:
#         model = Story
#         fields = (
#             'category',
#             'author',
#             'tags',
#             'title',
#             'slug',
#             'image',
#             'cover_image',
#             'content',
#             'created_at',
#             'updated_at',
#         ) 