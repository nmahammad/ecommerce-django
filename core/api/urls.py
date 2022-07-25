from django.urls import path
from core.api.views import SubscriberView

urlpatterns = [
    path('subscribers/' , SubscriberView.as_view())
]

