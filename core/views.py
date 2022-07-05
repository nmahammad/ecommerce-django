from dataclasses import fields
from multiprocessing import context
from re import template
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib import messages

from django.urls import reverse_lazy
from core.forms import ContactForm
from core.models import Contact


from django.http import HttpResponse
from core.models import Contact
# Create your views here.


def error_404(request):
    return render(request, '404.html')


def about(request):
    return render(request, 'about-page.html')


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


def index(request):
    return render(request, 'index.html')
