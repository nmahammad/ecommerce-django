from pyexpat import model
from rest_framework import serializers
from core.models import NewSubscriber

class SubscriberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NewSubscriber
        fields = {
            'email',
        }
