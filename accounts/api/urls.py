from django.urls import path
from accounts.api.views import(
 registration_view
)


urlpatterns = [
 path("register", registration_view, name='register'),
]

