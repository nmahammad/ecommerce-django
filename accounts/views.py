from requests import request
from accounts.forms import LoginForm
from accounts.tasks import send_email_confirmation

from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from django.views.generic import CreateView, View
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView, PasswordResetConfirmView
from django.contrib.auth import get_user_model, authenticate, login as django_login, logout as django_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from accounts.utils import account_activation_token

from accounts.forms import (RegisterForm, ResetPasswordForm,
                            LoginForm, CustomPasswordChangeForm,
                            CustomSetPasswordForm
                            )

User = get_user_model()


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'login.html'
    form_class = CustomSetPasswordForm
    success_url = reverse_lazy('home')

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS,
                             'Sizin yeni sifreniz teyin edildi')
        return super().get_success_url()


class ResetPasswordView(PasswordResetView):
    template_name = 'login.html'
    form_class = ResetPasswordForm
    email_template_name = 'email/reset-password-mail.html'
    success_url = reverse_lazy('home')

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS,
                             'Emailinizi yoxlayin!')
        return super().get_success_url()


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

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
                                 'Mail hesabiniz artiq aktiv olunmusdur')
            return redirect(reverse_lazy('login'))
        elif user is not None and account_activation_token.check_token(user, token):
            messages.add_message(request, messages.SUCCESS,
                                 'Mail hesabiniz tesdiq olundu')
            user.is_active = True
            user.save()
            return redirect(reverse_lazy('login'))
        else:
            messages.add_message(request, messages.SUCCESS,
                                 'Mail hesabiniz tesdiq olunmadi')
            return redirect(reverse_lazy('home'))

        



### Login 

class MultikartLoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = reverse_lazy('/')

    # def get(self, request , *args, **kwargs):
    #     if request.method == 'POST' and 'login-button' in request.POST:
    #         pass

    # def post(self, request, *args, **kwargs):
  
    #     form = self.get_form()
    #     if form.is_valid():
    #         return self.form_valid(form)
    #     else:
    #         return self.form_invalid(form)

    
    


# def login(request):
#     form = LoginForm()

#     if request.method == 'POST' and 'login-button' in request.POST:
#         form = LoginForm(data=request.POST)
#         if form.is_valid():
#             user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
#             if user is not None:
#                 django_login(request, user)
#                 messages.add_message(request, messages.SUCCESS, 'Ugurla login oldunuz')
#                 return redirect('/') 
#             else:
#                 messages.add_message(request, messages.ERROR, 'Username ve ya password sehvdir!')
#     context = {
#         'form': form
#     }
#     return render(request, 'login.html', context)


@login_required
def user_profile(request):
    return render(request, 'profile.html')


@login_required
def logout(request):
    django_logout(request)
    return redirect('/')


## Change password

class ChangePasswordView(LoginRequiredMixin, PasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name = 'login.html'
    success_url = reverse_lazy('login')

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS,
                             'Ugurla sifreniz deyisdi')
        return super().get_success_url()
