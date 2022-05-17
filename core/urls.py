from django.urls import path
from core.views import about,error_404,contact,faq, index

urlpatterns = [

    path('error/' , error_404),
    path('about/' , about),
    path('contact/' , contact, name='contact'),
    path('faq/' , faq),
    path('' , index, name="home"),
]