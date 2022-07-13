from unittest import result
from django.test import TestCase
from django.urls import reverse_lazy



class TestProductsAPIView(TestCase):

 @classmethod
 def setUpClass(cls):
  cls.url = reverse_lazy('product-list')
  cls.valid_data = {
    "category_id": 1,
    "vendor_id" : 1,
    "brand_id": 1
  }


 def test_api_url(self):
  expected_url = '/api/products/'
  self.assertEqual(self.url, expected_url)

#  def test_apii_post_request_status_code(self):
#   res = self.client.get(self.url,data=self.valid_data)
#   print(res.json())
#   self.assertEqual(res.status_code, 201)

#  def test_api_gett_request_response(self):
#   res = self.client.post(self.url, data=self.valid_data)
#   result=res.json()
#   self.assertEqual(result['category_id'],self.valid_data['category_id'])

 def test_api_post_request_status_code(self):
  res = self.client.get(self.url)
  self.assertEqual(res.status_code, 200)

 def test_api_get_request_response(self):
  res = self.client.get(self.url)
  self.assertIsInstance(res.json(), list)

 @classmethod
 def tearDownClass(cls):
     ... 