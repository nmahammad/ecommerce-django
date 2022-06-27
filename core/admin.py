from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

#Register your models here.
from core.models import Contact,Faq,NewSubscriber
admin.site.register([Contact, Faq,NewSubscriber])

