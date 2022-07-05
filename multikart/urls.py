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
from order.views import addtoshopcart
from django.urls import include, path, re_path


from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi



# schema_view = get_schema_view(
#     openapi.Info(
#         title="Snippets API",
#         default_version='v1',
#         description="Test description",
#         terms_of_service="https://www.google.com/policies/terms/",
#         contact=openapi.Contact(email="contact@snippets.local"),
#         license=openapi.License(name="BSD License"),
#     ),
#    public=True,
#    permission_classes=[permissions.AllowAny],
# )


    
urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),

    path("api/", include('product.api.urls')),

    path("api/", include('core.api.urls')),
    path("api/", include('accounts.api.urls')),
    path('admin/', admin.site.urls),
    # re_path('^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    # re_path('^swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    
    path('admin/', admin.site.urls),

    path('addtoshopcart/<int:id>', addtoshopcart, name='addtoshopcart'),

    path('', include('social_django.urls', namespace='social')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += i18n_patterns(
    
    
    
    path('', include('order.urls')),

    path('', include('accounts.urls')),

    path('', include('core.urls')),

    path('', include('product.urls')),

    path("api/accounts/", include('accounts.api.urls')),

)

