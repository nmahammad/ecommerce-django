from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from product.models import Category



# class Parent_idSerializer(serializers.ModelSerializer):
#  class Meta:
#   model = Category
#   fields = (
#    'title',
#   )




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

################################################

class CategoryReadSerializer(serializers.ModelSerializer):
 parent_id = serializers.SerializerMethodField()
 # parent_id = serializers.CharField(source='parent_id.title')


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