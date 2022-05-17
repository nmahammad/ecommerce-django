from multiprocessing import context
from pyexpat import model
from re import template
from django.shortcuts import render, redirect
from django.contrib import messages

from django.urls import reverse_lazy
from django.http import HttpResponse
from product.forms import ReviewForm, SearchForm
from core.models import Contact
from django.views.generic import View , ListView, DetailView, CreateView
from product.models import Product , Brand, ProductVersion, Review
from django.shortcuts import get_object_or_404


# Create your views here.

# def category(request):
#     new_products = Product.objects.all().order_by('-created_at')[:2]
#     products = Product.objects.all()


#     context = {
#         'products': products,
#         'new_products' : new_products,
#     }

#     return render(request,'category-page.html', context)


class CategoryListView(ListView):
    model = Product
    template_name = 'category-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        new_products = Product.objects.all().order_by('-created_at')[:2]
        products = Product.objects.all().order_by('created_at')
        context['new_products'] = new_products
        context['products'] = products

        # context['product_sizes'] =  product_version.property_value.filter(property_name_id__name='Size')
        
        return context







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


def profile(request):
    return render(request,'profile.html',)


def product_detail(request, id):
    new_products = Product.objects.all().exclude(id = id).order_by('-created_at')[:4]        

    product = get_object_or_404(Product, id=id)
    all_brands = Brand.objects.all()

    product_version = ProductVersion.objects.get(product_id=id)
    product_colors = product_version.property_value.filter(property_name_id__name='Color')
    product_sizes =  product_version.property_value.filter(property_name_id__name='Size')
    
    context = {
        'new_products' : new_products,
        'product': product,
        'all_brands' : all_brands,
        'product_colors' : product_colors,
        'product_sizes' : product_sizes,
    }

    return render(request, 'product-page.html', context)

