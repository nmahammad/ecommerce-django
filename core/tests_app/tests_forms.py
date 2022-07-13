import imp
from operator import imod
from django.test import TestCase
from core.forms import ContactForm


class TestContactForm(TestCase):

 @classmethod
 def setUpClass(cls):
  cls.valid_data = {
   "first_name" : "Kamran",
   "last_name" : "Aliyev",
   "email" : "aliyev@gmail.com",
   "phone_number" : "05155",
   "message" : "Hello.",
  }

  cls.invalid_data = {
   'name': """
   Lorem Ipsum is simply dummy text of the printing and typesetting 
   industry. Lorem Ipsum has been the industry's standard dummy text 
   ever since the 1500s, when an unknown printer took a galley of type 
   and scrambled it to make a type specimen book. It has survived not only 
   five centuries, but also the leap into electronic typesetting, remaining 
   essentially unchanged. It was popularised in the 1960s with the release of 
   """,
   "last_name" : "Aliyev",
   "email" : "aliyev",
   "phone_number" : "05155",
   "message" : "Hello",
  }
  cls.valid_form = ContactForm(data=cls.valid_data)
  cls.in_valid_form = ContactForm(data=cls.invalid_data)

 def test_form_with_valid_data(self):
  self.assertTrue(self.valid_form.is_valid())

 def test_form_with_invalid_data(self):
  self.assertFalse(self.in_valid_form.is_valid())

 def test_error_email(self):
  self.assertIn('email',self.in_valid_form.errors)
  self.assertIn('message',self.in_valid_form.errors)

 def test_error_message(self):
  self.assertIn('message',self.in_valid_form.errors)


 @classmethod
 def tearDownClass(cls):
     ... 