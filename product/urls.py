
from django.urls import path
from product.views import search,product_review,vendor , ProductDetailView, CategoryListView,export
from product.tasks import send_mail_to_subscribers

urlpatterns = [

    path('product/' , product_review ,name='product'),                
    path('search/' , search),                       
    path('vendor/' , vendor),                       
    path('product/<int:pk>/', ProductDetailView.as_view(), name="product_detail"),
    path('category/' ,CategoryListView.as_view(),name='category'),
    path('export/' ,export,name='export'),
    path('subscribers/' ,send_mail_to_subscribers,name='subscribers'),

]