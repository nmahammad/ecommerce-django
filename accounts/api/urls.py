from django.urls import path
from accounts.api.views import(
Register,
)

urlpatterns = [
 path('register', Register.as_view(), name='register'),
]
