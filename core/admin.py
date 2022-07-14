from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

#Register your models here.
from core.models import Contact,Faq,NewSubscriber, TeamMember
admin.site.register([Contact, Faq,NewSubscriber , TeamMember])

