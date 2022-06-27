import json
from multiprocessing import context
from pyexpat import model
from re import X, template
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.contrib import messages
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.http import HttpResponse
from requests import request
from product.forms import ReviewForm, SearchForm
from product.tasks import process_func
from core.models import Contact
from django.views.generic import View, ListView, DetailView, CreateView
from product.models import Product, Brand, ProductVersion, Review, PropertyValue, PropertyName
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


class CategoryListView(ListView):
    model = Product
    template_name = 'category-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        new_products = Product.objects.all().order_by('-created_at')[:2]
        products = Product.objects.all().order_by('created_at')
        context['new_products'] = new_products
        context['products'] = products
        context['categories'] = Product.objects.distinct().values('category_id__title' , 'category_id__id')
        context['brands'] = Product.objects.distinct().values('brand_id__title' , 'brand_id__id')
        context['product_colors'] = PropertyValue.objects.filter(property_name_id__name='Color')
        
        return context


def product_review(request):
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 "Your message has been saved")
            return redirect(reverse_lazy('product'))
    context = {
        'form': form
    }
    return render(request, 'product-page.html', context)


def search(request):
    return render(request, 'search.html')


def vendor(request):
    return render(request, 'vendor-profile.html',)


def profile(request):
    return render(request, 'profile.html',)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product-page.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_pk = self.kwargs['pk']
        product = self.get_object()
        context['new_products'] = Product.objects.all().exclude(
            id=product_pk).order_by('-created_at')[:4]
        context['related_products'] = Product.objects.filter(
            category_id=product.category_id).exclude(id=product_pk).order_by('?')[:4]

        
        context['product_sizes'] = product.main_version.property_value.filter(
             property_name_id__name='Size')

        product_versions = ProductVersion.objects.filter(product_id=product_pk) 

        product_colors = []
        for pv in list(product_versions):
            pc = pv.property_value.filter(property_name_id__name='Color').values_list('name')
            product_colors.append(pc[0][0])

        context['product_colors'] = product_colors
    
        context['brands'] = Brand.objects.all().order_by('?')[:4]

        if(product.main_version.discount_id) :
            old_price = ( product.main_version.price // (100 - product.main_version.discount_id.percentage) )*100
            percentage = product.main_version.discount_id.percentage 
            context['old_price'] = old_price
            context['percentage'] = percentage

        return context

    def get_queryset(self):
        brand_id = self.request.GET.get('brand_id')
        queryset = super().get_queryset()
        if brand_id:
            queryset = queryset.filter(brand__id=brand_id)
        return queryset

    def related_products(self, request):
        product = self.get_object()
        related_products = Product.objects.filter(
            category_id=product.category_id).exclude(id=self.kwargs['pk']).order_by('?')[:12]
        paginator = Paginator(related_products, 4)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request=request, template_name="product-page.html", context={'related_products': page_obj})



def export(request):
    process_func.delay()
    return redirect('/')


