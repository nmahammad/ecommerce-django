from itertools import product
import json
from multiprocessing import context
from pyexpat import model
from re import X, template
from unicodedata import category
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
from product.models import Product, Brand, ProductVersion, Review,  Color, Size, Category
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
        context['categories'] = Category.objects.filter(parent_id = None)
        context['brands'] = Brand.objects.distinct()
        context['product_colors'] = Color.objects.all()
        context['product_sizes'] = Size.objects.all()


        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        brand_id = self.request.GET.get('brand_id')  # 1
        category_id = self.request.GET.get('category_id')
        if brand_id:
            queryset = queryset.filter(brand_id__id=brand_id)
        if category_id:
            queryset = queryset.filter(category_id__parent_id=category_id)
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
    model = ProductVersion
    template_name = 'product-page.html'
    context_object_name = 'product_version'
    form_class = ReviewForm

    def get_context_data(self, **kwargs):
        self.object = self.get_object()
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        product_version = self.get_object()
        product_pk = product_version.product_id.id
        product_version_pk = product_version.id
        context['u'] = self.request.user.id
        product = self.get_object().product_id
        context['product'] = product
        context['new_products'] = Product.objects.all().exclude(id=product_pk).order_by('-created_at')[:4]

        context['related_products'] = Product.objects.filter(
            category_id=product_version.product_id.category_id).exclude(id=product_pk).order_by('?')[:4]

        context['reviews'] = Review.objects.filter(product_id=product_pk)
        context['review_count'] = Review.objects.filter(product_id=product_pk).count()

        context['brands'] = Brand.objects.all().order_by('?')[:4]

        product_versions = ProductVersion.objects.filter(product_id=product_pk)
        context['product_versions'] = product_versions

        context['distinct_product_versions'] = ProductVersion.objects.filter(product_id=product_pk).distinct('color')

        # product_colors = []
        # for pv in product_versions:
        #     product_colors.append(pv.color)

        # def unique_colors(l):
        #     output = []
        #     for x in l:
        #         if x not in output:
        #             output.append(x)
        #     return output
        
        # context['product_colors'] = unique_colors(product_colors)

        related_versions = []
        for pv in product_versions:
            if pv.color:
                if pv.color.id == product_version.color.id:
                    related_versions.append(pv)  
            
        # product_sizes = []
        # if pv.size:
        #     for pv in related_versions:
        #         product_sizes.append(pv.size)
        # context['product_sizes'] = product_sizes

        context['related_versions'] = related_versions

        # if (product_version.in_wishlist == self.request.user.id):
        #     a =1
        # else:
        #     a = 0
        # context['a'] = a

        if(product_version.discount_id):
            percentage = product_version.discount_id.percentage
            new_price = product_version.price - (product_version.price * percentage) // 100

            context['new_price'] = new_price
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
        form.instance.product_id = self.get_object().product_id
        form.instance.user_id = self.request.user
        
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)


def export(request):
    process_func.delay()
    return redirect('/')



