from operator import concat
from django.test import TestCase
from core.models import Contact

class ContactTest(TestCase):

  def setUp(self):
   self.data1 = {
    "first_name" : "Kamran",
    "last_name" : "Aliyev",
    "email" : "aliyev@gmail.com",
    "phone_number" : "05155",
    "message" : "Hello",
   }

   self.data2 = {
    "first_name" : "Kamran2",
    "last_name" : "Aliyev2",
    "email" : "aliyev2@gmail.com",
    "phone_number" : "05155",
    "message" : "Hello",
   }

   self.contact1 = Contact.objects.create(**self.data1)
   self.contact2 = Contact.objects.create(**self.data2)


  def test_model_data(self):
   self.assertEqual(self.data1['first_name'], self.contact1.first_name)
   self.assertEqual(self.data1['email'], self.contact1.email)

  def test_str_method(self):
   self.assertEqual(str(self.contact1), self.data1['first_name'] + " " + self.data1['last_name'])


  def tearDown(self):
    del self.contact1
    del self.contact2