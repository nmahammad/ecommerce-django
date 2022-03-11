from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def category(request):
 return render(request,'category-page.html',)


def product(request):
 return render(request,'product-page.html',)



def search(request):
 return render(request,'search.html',)


def vendor(request):
 return render(request,'vendor-profile.html',)
