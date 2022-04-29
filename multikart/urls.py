"""multikart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from core.views import error_404, about, ContactView, faq, index
from product.views import category,product, search, vendor
from accounts.views import login, profile,logout
from user.views import forgetPwd
from django.conf import settings
from django.urls import include, path
from order.views import cart_products, checkout, order_success, wish_list
# from user.views import profile
from product.views import category,product,search,vendor, product_detail, BrandListView
from accounts.views import login, forget_password, register

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    # path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    path('admin/', admin.site.urls),
    path('', include('social_django.urls', namespace='social')),
    path('cart/' , cart_products),
    path('checkout/' , checkout ),
    path('order-success/' , order_success, name='order-success'),
    path('wishlist/' , wish_list),
    path('forgetpwd/', forgetPwd),
    path('login/' , login, name='login'),
    path('logout/', logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('register/', register),
    path('error/' , error_404),
    path('about/' , about),
    path('contact/' , ContactView.as_view(), name='contact'),
    path('faq/' , faq),
    path('register/' , register),
    path('' , index, name="/"),
    path('forget-password/' , forget_password),
    path('category/' , category),
    path('product/' , product ,name='product'),              #in this page you can see the products
    path('search/' , search),                                #in this page you can filter and search peoducts
    path('vendor/' , vendor),                                #in this page you can see the vendor profile
    path('profile/' , profile),                              #in this page, contact and billing details models exist
    path('accounts/', include('accounts.urls')),   
    path('product/<int:id>/', product_detail, name='product_detail'),
    path('brands/' , BrandListView.as_view(), name = "brands" ),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



