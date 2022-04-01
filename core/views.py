from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib import messages

from django.urls import reverse_lazy
from core.forms import ContactForm


# Create your views here.

def error_404(request):
    return render(request, '404.html' )


def about(request):
    return render(request, 'about-page.html' )


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Your message has been saved")
            return redirect(reverse_lazy('contact'))
    context = {
        'form': form
    }
    return render(request, 'contact.html',context)


def faq(request):
    return render(request, 'faq.html' )


def index(request):
    return render(request, 'index.html' )
