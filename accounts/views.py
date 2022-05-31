from audioop import reverse
from django.http import HttpResponseRedirect
from requests import request
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView, PasswordResetConfirmView
from django.contrib.auth import get_user_model, authenticate, logout as django_logout

from django.shortcuts import render, redirect

from django.urls import reverse_lazy

from django.views.generic import CreateView, View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView
from django.views.generic import View
from accounts.forms import LoginForm, CustomPasswordChangeForm
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from accounts.utils import account_activation_token

from accounts.tasks import send_email_confirmation


from accounts.forms import (RegisterForm, ResetPasswordForm,
                            LoginForm, CustomPasswordChangeForm,
                            CustomSetPasswordForm
                            )

User = get_user_model()


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.instance
        user.set_password(form.cleaned_data['password'])
        user.is_active = False
        user.save()
        current_site = self.request.META['HTTP_HOST']
        send_email_confirmation(user, current_site)
        return response


class Activate(View):
    def get(self, request, *args, **kwargs):
        uidb64 = kwargs.get('uidb64')
        token = kwargs.get('token')
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user.is_active:
            messages.add_message(request, messages.SUCCESS,
                                 'Your account is active')
            return redirect(reverse_lazy('login'))
        elif user is not None and account_activation_token.check_token(user, token):
            messages.add_message(request, messages.SUCCESS,
                                 'Mail address is verified')
            user.is_active = True
            user.save()
            return redirect(reverse_lazy('login'))
        else:
            messages.add_message(request, messages.SUCCESS,
                                 'Mail address is not verified')
            return redirect(reverse_lazy('home'))


# Login

class MultikartLoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'

    def dispatch(self, request, *arg, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super().dispatch(request, *arg, **kwargs)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST' and 'login-button' in request.POST:
            LoginForm(data=request.POST)
        return super().post(request, *args, **kwargs)
         

@login_required
def user_profile(request):
    return render(request, 'profile.html')


# @login_required
# def logout(request):
#     django_logout(request)
#     return redirect('/')


class MulticartLogoutView(LogoutView):
    def get(self, request):
        django_logout(request)
        return reverse_lazy('/en/login')


from accounts.forms import RegisterForm



# # Create your views here.
# def register(request):
#     register_form = RegisterForm()
#     if request.method == 'POST' and "register" in request.POST:
#         register_form = RegisterForm(data=request.POST)
#         if register_form.is_valid():
#             user = register_form.save(request)
#             user.username = 'user_' + str(user.id)
#             user.set_password(register_form.cleaned_data['password'])
#             user.save()
#             return redirect('/')
    
#     context = {
#         'register_form' : register_form
#     }
#     return render(request , 'register.html' , context)

@login_required
def logout(request):
    django_logout(request)
    return redirect('login')


# Reset password

class ResetPasswordView(PasswordResetView):
    template_name = 'forget_pwd.html'
    form_class = ResetPasswordForm
    email_template_name = 'email/reset-password-mail.html'
    success_url = reverse_lazy('login')

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS,
                             'Check your e-mail')
        return super().get_success_url()


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'login.html'
    form_class = CustomSetPasswordForm
    success_url = reverse_lazy('home')

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS,
                             'Your new password is ready')
        return super().get_success_url()


# Change Password


class ChangePasswordView(LoginRequiredMixin,PasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name = 'password-change.html'
    success_url = reverse_lazy('login')

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS,
                             'Password has been changed successfully')
        return super().get_success_url()
