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
from django import views
from django.contrib import admin
# from accounts.views import user_profile,logout
from django.conf import settings
from django.urls import include, path


from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import ChangePasswordView, MulticartLogoutView
from core.views import ContactView
from product.views import CategoryListView







    
urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),
    path("api/", include('product.api.urls')),
    path("api/", include('multikart.api.urls')),
    path('admin/', admin.site.urls),
    
    path('', include('social_django.urls', namespace='social')),

    

    


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(
    path('logout/', MulticartLogoutView.as_view(), name='logout'),
    
    path('', include('order.urls')),

    path('', include('accounts.urls')),

    path('', include('core.urls')),

    path('', include('product.urls')),
)

