import imp
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View 
from product.models import Product , Brand, ProductVersion, Review
from django.shortcuts import get_object_or_404

# Create your views here.

def category(request):
 return render(request,'category-page.html',)


def product(request):
 return render(request,'product-page.html',)


def search(request):
 return render(request,'search.html',)


def vendor(request):
    return render(request,'vendor-profile.html',)


def profile(request):
    return render(request,'profile.html',)


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    brands = Brand.objects.all().order_by('?')[:4]
    all_brands = Brand.objects.all()

    product_version = ProductVersion.objects.get(id=id)
    product_colors = product_version.property_value.filter(property_name_id__name='Color')
    product_sizes =  product_version.property_value.filter(property_name_id__name='Size')
    related_products = Product.objects.filter(category_id=product.category_id).exclude(id=id)[:4]

    context = {
        'product': product,
        'brands' : brands,
        'all_brands' : all_brands,
        'product_colors' : product_colors,
        'product_sizes' : product_sizes,
        'related_products' : related_products,
    }

    return render(request, 'product-page.html', context)
    

# def single_product(request, id=1):
#     relatedproducts = ProductVersion.objects.all()
#     singleproduct = ProductVersion.objects.get(id=id)
#     product_reviews = Review.objects.all()
#     product_colors = singleproduct.property.filter(property_name__name='color')
#     product_sizes =  singleproduct.property.filter(property_name__name='size')
    
#     context = {
#         'related_products': relatedproducts,
#         'product_version': singleproduct,
#         'colors' : product_colors,
#         'sizes' : product_sizes,
#         'reviews' : product_reviews,
#         }
#     return render(request,'product-page.html', context)

