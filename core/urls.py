from django.urls import path
from core.views import AboutView,error_404,faq, MainPageView, ContactView

urlpatterns = [

    path('error/' , error_404),
    path('about/' ,AboutView.as_view()  , name='about'),
    path('faq/' , faq, name='faq'),
    path('contact/' , ContactView.as_view(), name='contact'),
    path('' , MainPageView.as_view(), name="home"),
]