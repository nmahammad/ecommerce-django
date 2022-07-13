from django.test import TestCase
from django.urls import reverse_lazy



class TestContactView(TestCase):

 @classmethod
 def setUpClass(cls):
  cls.contact_page_url = reverse_lazy('contact')
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

 def test_url(self):
  expected_contact_url = '/en/contact/'
  self.assertEqual(self.contact_page_url, expected_contact_url)

 def test_contact_page_template_name(self):
  res = self.client.get(self.contact_page_url)
  self.assertTemplateUsed(res, 'contact.html')

 def test_contact_page_context(self):
  res = self.client.get(self.contact_page_url)
  self.assertTrue(res.context['form'])


 def test_contact_page_post_request_status_code(self):
  res = self.client.post(self.contact_page_url, self.valid_data)
  self.assertRedirects(res, reverse_lazy('contact'), )

 def test_contact_page_post_request_invalid_data(self):
  res = self.client.post(self.contact_page_url, self.invalid_data)
  form = res.context['form']
  self.assertTrue(form.errors)


 @classmethod
 def tearDownClass(cls):
     ... 
  
