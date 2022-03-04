from django.shortcuts import render

# Create your views here.

def error_404(request):
    return render(request, '404.html' )


def about(request):
    return render(request, 'about-page.html' )


def contact(request):
    return render(request, 'contact.html' )


def faq(request):
    return render(request, 'faq.html' )


def index(request):
    return render(request, 'index.html' )
