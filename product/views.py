from multiprocessing import context
from pyexpat import model
from re import template
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator

from django.urls import reverse_lazy
from django.http import HttpResponse
from requests import request
from product.forms import ReviewForm, SearchForm
from product.tasks import process_func
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



def product_review(request):
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
    query=request.GET['k']
    products = ProductVersion.objects.filter(title__icontains=query).order_by('id')

    # search= SearchForm()
    # if request.method == 'GET':
    #     search = SearchForm(data=request.GET)
    #     print(request.GET.get('search'))
    #     # result = ProductVersion.objects.filter(title__icontains=request.GET.get('search'))
    #     result = Contact.objects.filter(first_name__icontains=request.GET.get('search'))
    #     print(result)
    # context = {
    #     'form': search
    # }
    return render(request,'search.html',{'products':products})


def vendor(request):
    return render(request,'vendor-profile.html',)


def profile(request):
    return render(request,'profile.html',)



class ProductDetailView(DetailView):
    model = Product
    template_name = 'product-page.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_pk = self.kwargs['pk'] 
        product = self.get_object()
        context['new_products'] = Product.objects.all().exclude( id = product_pk  ).order_by('-created_at')[:4]  
        context['related_products'] = Product.objects.filter(category_id = product.category_id ).exclude( id = product_pk  ).order_by('?')[:4]

        product_version = ProductVersion.objects.get( product_id = product_pk )
        context['product_sizes'] =  product_version.property_value.filter(property_name_id__name='Size')
        context['product_colors'] = product_version.property_value.filter(property_name_id__name='Color')
        
        context['brands'] = Brand.objects.all().order_by('?')[:4]

        return context
    
    def get_queryset(self):
        brand_id = self.request.GET.get('brand_id')
        queryset = super().get_queryset()
        if brand_id:
            queryset = queryset.filter(brand__id = brand_id )
        return queryset
    
    def related_products(self, request):
        product = self.get_object()
        related_products = Product.objects.filter(category_id = product.category_id ).exclude( id = self.kwargs['pk']   ).order_by('?')[:12]
        paginator = Paginator(related_products, 4)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request=request, template_name="product-page.html", context={'related_products':page_obj})



def export (request):
    process_func.delay()
    return redirect ('/')