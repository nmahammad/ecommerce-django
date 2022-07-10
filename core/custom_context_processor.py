from core.models import NewSubscriber
from core.forms import SubscriberForm
from django.shortcuts import render

def subscriber_renderer(request):
    subscriber_form = SubscriberForm()
    if request.method == 'POST' and 'susbcribe-button' in request.POST:
        subscriber_form = SubscriberForm(data=request.POST)
        if subscriber_form.is_valid():
            subscriber_form.save()
    context = {
        'subscriber_form': subscriber_form
    }
    return context




