from dataclasses import fields
from itertools import product
from multiprocessing import context
from re import template
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib import messages

from django.urls import reverse_lazy
from core.forms import ContactForm
from core.models import Contact
from django.views.generic import ListView, DetailView
from product.models import Product, ProductVersion
from core.models import TeamMember
from django.http import HttpResponse
from core.models import Contact
# Create your views here.


def error_404(request):
    return render(request, '404.html')


class AboutView(ListView):
    model = TeamMember
    template_name = 'about-page.html'
    context_object_name = 'members'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['members'] = TeamMember.objects.all()

        return context



# def contact(request):
#     form = ContactForm()
#     if request.method == 'POST':
#         form = ContactForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.add_message(request, messages.SUCCESS, "Your message has been saved")
#             return redirect(reverse_lazy('contact'))
#     contacts_list = Contact.objects.all()
#     context = {
#         'form': form,
#         'contacts' : contacts_list,

#     }
#     return render(request, 'contact.html',context)


class ContactView(CreateView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.add_message(self.request, messages.SUCCESS,
                             "Your message has been saved")
        return result


def faq(request):
    return render(request, 'faq.html')


class MainPageView(ListView):
    model = Product
    template_name = 'index.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['new_products'] = Product.objects.all().order_by('-created_at')[:2]
        product_versions = ProductVersion.objects.all()
        context['product_versions'] = product_versions
        context['featured_products'] = Product.objects.filter(featured=True)[:6]

        return context

