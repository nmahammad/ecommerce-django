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
from django.urls import path, include
from order.views import cart_products, checkout, order_success, wish_list
from core.views import error_404, about, contact, faq, index
from user.views import login, profile,register,forgetPwd
from product.views import category,product, search, vendor


urlpatterns = [
    # path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    # path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    path('admin/', admin.site.urls),
    path('cart/' , cart_products),
    path('checkout/' , checkout ),
    path('order-success/' , order_success),
    path('wishlist/' , wish_list),
    path('forgetpwd/', forgetPwd),
    path('login/' , login),
    path('profile/', profile),
    path('register/', register),
    path('error/' , error_404),
    path('about/' , about),
    path('contact/' , contact, name='contact'),
    path('faq/' , faq),
    path('' , index, name='home'),
    path('category/', category),
    path('product/', product,name='product'),
    path('search/' , search),
    path('vendor/',vendor),
    
]



