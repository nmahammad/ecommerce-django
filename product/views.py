from multiprocessing import context
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib import messages

from django.urls import reverse_lazy
from django.http import HttpResponse
from product.forms import ReviewForm, SearchForm
from product.models import ProductVersion
from core.models import Contact

# Create your views here.

def category(request):
    product_version = ProductVersion.objects.all().order_by('-created_at')[:1]


    context = {
        'product_version': product_version,

    }

    return render(request,'category-page.html',context)





def product(request):
 form= ReviewForm()
 if request.method == 'POST':
        form = ReviewForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Your message has been saved")
            return redirect(reverse_lazy('product'))
 context = {
        'form': form
    }
 return render(request,'product-page.html',context)



def search(request):
    search= SearchForm()
    if request.method == 'GET':
        search = SearchForm(data=request.GET)
        print(request.GET.get('search'))
        # result = ProductVersion.objects.filter(title__icontains=request.GET.get('search'))
        result = Contact.objects.filter(first_name__icontains=request.GET.get('search'))
        print(result)
    context = {
        'form': search
    }
    return render(request,'search.html', context)


def vendor(request):
    return render(request,'vendor-profile.html',)



