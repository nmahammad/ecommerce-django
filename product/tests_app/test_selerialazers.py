import imp
from operator import imod
from django.test import TestCase
from product.api.serializers import CategoryCreateSerializer


class TestCategoryCreateSerializer(TestCase):

 @classmethod
 def setUpClass(cls):
  cls.valid_data = {
   "title" : "car",
  }

  cls.invalid_data = {
   "title" : """
   Lorem Ipsum is simply dummy text of the printing and typesetting 
   industry. Lorem Ipsum has been the industry's standard dummy text 
   ever since the 1500s, when an unknown printer took a galley of type 
   and scrambled it to make a type specimen book. It has survived not only 
   five centuries, but also the leap into electronic typesetting, remaining 
   essentially unchanged. It was popularised in the 1960s with the release of 
   """,
  }
  cls.valid_form = CategoryCreateSerializer(data=cls.valid_data)
  cls.in_valid_form = CategoryCreateSerializer(data=cls.invalid_data)

 def test_form_with_valid_data(self):
  self.assertTrue(self.valid_form.is_valid())

 def test_form_with_invalid_data(self):
  self.assertFalse(self.in_valid_form.is_valid())



 @classmethod
 def tearDownClass(cls):
     ... 