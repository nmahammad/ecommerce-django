from django.shortcuts import render
from django.http import HttpResponse
from core.models import Contact 
# Create your views here.

def error_404(request):
    return render(request, '404.html' )


def about(request):
    return render(request, 'about-page.html' )


def contact(request):
    contacts_list = Contact.objects.all()
    context = {
        'contacts' : contacts_list
    }
    return render(request, 'contact.html' , context)


def faq(request):
    return render(request, 'faq.html' )


def index(request):
    return render(request, 'index.html' )
