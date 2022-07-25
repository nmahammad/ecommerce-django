from rest_framework.generics import CreateAPIView
from core.models import NewSubscriber 
from core.api.serializers import SubscriberSerializer


class SubscriberView(CreateAPIView):
    queryset = NewSubscriber.objects.all()
    serializer_class = SubscriberSerializer

