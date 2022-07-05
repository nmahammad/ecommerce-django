from itertools import product
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
from django.views.generic import View, ListView, DetailView, CreateView, FormView
from product.models import Product, Brand, ProductVersion, Review, PropertyValue, PropertyName
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.http import HttpResponse, HttpResponseRedirect



class CategoryListView(ListView):
    model = Product
    template_name = 'category-page.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        new_products = Product.objects.all().order_by('-created_at')[:2]
        context['new_products'] = new_products
        context['categories'] = Product.objects.distinct().values(
            'category_id__title', 'category_id__id')
        # context['categories'] = Category.objects.filter(stories__isnull=False).distinct()
        context['brands'] = Product.objects.distinct().values(
            'brand_id__title', 'brand_id__id')
        context['product_colors'] = PropertyValue.objects.filter(
            property_name_id__name='Color')

        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        brand_id = self.request.GET.get('brand_id')  # 1
        if brand_id:
            queryset = queryset.filter(brand_id__id=brand_id)
        return queryset


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
    return render(request, 'vendor-profile.html',)


def profile(request):
    return render(request, 'profile.html',)


class ProductDetailView(CreateView, DetailView):
    model = Product
    template_name = 'product-page.html'
    context_object_name = 'product'
    form_class = ReviewForm

    def get_context_data(self, **kwargs):
        self.object = self.get_object()
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        product_pk = self.kwargs['pk']
        product = self.get_object()
        context['new_products'] = Product.objects.all().exclude(
            id=product_pk).order_by('-created_at')[:4]

        context['related_products'] = Product.objects.filter(
            category_id=product.category_id).exclude(id=product_pk).order_by('?')[:4]

        context['reviews'] = Review.objects.filter(product_id=product_pk)
        context['review_count'] = Review.objects.filter(
            product_id=product_pk).count()

        product_versions = ProductVersion.objects.filter(product_id=product_pk)
        context['product_versions'] = product_versions

        context['product_sizes'] = product.main_version.property_value.filter(
            property_name_id__name='Size')

        context['brands'] = Brand.objects.all().order_by('?')[:4]

        if(product.main_version.discount_id):
            old_price = (product.main_version.price // (100 -
                         product.main_version.discount_id.percentage))*100
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

    def get_success_url(self):
        product_id= self.get_object().id
        return reverse_lazy('product_detail', kwargs={'pk': product_id})

    def form_valid(self, form):
        form.instance.product_id = self.get_object()
        form.instance.user_id = self.request.user
        
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)


def export(request):
    process_func.delay()
    return redirect('/')



