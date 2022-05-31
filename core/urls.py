from django.urls import path
from core.views import about,error_404,faq, index, ContactView

urlpatterns = [

    path('error/' , error_404),
    path('about/' , about),
    path('faq/' , faq),
    path('contact/' , ContactView.as_view(), name='contact'),
    path('' , index, name="home"),
]