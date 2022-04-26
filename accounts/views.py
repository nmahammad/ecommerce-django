from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from accounts.forms import LoginForm



# Create your views here.
def login(request):
 form = LoginForm()
 next_page = request.GET.get('next', '/') # next='/accounts/profile/'
 if request.method == 'POST':
  form = LoginForm(data=request.POST)
  if form.is_valid():
   user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
   if user is not None:
    django_login(request, user)
    messages.add_message(request, messages.SUCCESS, 'Ugurla login oldunuz')
    return redirect(next_page)
   else:
    messages.add_message(request, messages.ERROR, 'Username ve ya password sehvdir!')
 context = {
    'form': form
   }
 return render(request,'login.html',context)



@login_required
def profile(request):
 return render(request,'profile.html',)



@login_required
def logout(request):
 django_logout(request)
 return redirect('/')
from django.shortcuts import redirect, render
from accounts.forms import RegisterForm

# Create your views here.
def register(request):
    register_form = RegisterForm()
    if request.method == 'POST' and "register" in request.POST:
        register_form = RegisterForm(data=request.POST)
        if register_form.is_valid():
            user = register_form.save(request)
            user.username = 'user_' + str(user.id)
            user.set_password(register_form.cleaned_data['password'])
            user.save()
            return redirect('/')
    
    context = {
        'register_form' : register_form
    }
    return render(request , 'register.html' , context)




def login(request):
    return render(request,'login.html',)


def forget_password(request):
    return render(request, 'forget_pwd.html' )

