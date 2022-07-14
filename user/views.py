from multiprocessing import context
from django import views
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from user.models import WishList, WishListItem
from product.models import ProductVersion
from django.views.generic import ListView
# Create your views here.


def forgetPwd(request):
 return render(request,'forget_pwd.html',)



def register(request):
 return render(request,'register.html',)

 
def profile(request):
 return render(request,'profile.html',)





    

