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
from core.views import error_404, about, contact, faq, index
from product.views import category,product, search, vendor
from accounts.views import user_profile,logout
from user.views import forgetPwd
from django.conf import settings
from django.urls import include, path
from product.views import category,product,search,vendor, ProductDetailView


from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('social_django.urls', namespace='social')),

    path('', include('order.urls')),

    path('', include('accounts.urls')),

    path('profile/', user_profile, name='profile'),
    path('error/' , error_404),
    path('about/' , about),
    path('contact/' , contact, name='contact'),
    path('faq/' , faq),
    path('' , index, name="home"),

    path('category/' , category , name = 'products_page'),
    path('product/' , product ,name='product'),                
    path('search/' , search),                       
    path('vendor/' , vendor),                       
    path('product/<int:pk>/', ProductDetailView.as_view(), name="product_detail"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



