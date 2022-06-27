from django.urls import path
from accounts.api.views import(
    registration_view
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from accounts.api.views import UserProfileAPIView

urlpatterns = [
    path("register", registration_view, name='register'),  
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('me/', UserProfileAPIView.as_view(), name='me'),
] 
