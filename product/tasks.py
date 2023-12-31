import time
from datetime import datetime, timezone, timedelta
from celery import shared_task
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

from accounts.models import User
from product.models import Product 
from product.publisher import Publish 
# from product import
# from product.models import 

@shared_task
def process_func():
 time.sleep(10)
 return 'Proces done'


#test

@shared_task
def send_mail_to_subscribers():
    email_list = []
    now = datetime.now(timezone.utc) - timedelta(days=0)
    email_list = User.objects.filter(is_active=True, last_login__lte=now).values_list('email', flat=True)
    new_products = Product.objects.all().order_by('-created_at')[:2]
    # email_list = User.objects.filter(is_active=True).values_list('email',flat=True)
    mail_text = render_to_string('email-subscribers.html', {
        'new_products': new_products, 
    })
    print(email_list)
    # mail_text = "salam"
    Publish(data={"body": mail_text, "subject": "new_products", "recipients": list(email_list), "subtype": "html"  }, event_type="send_mail")

    # msg = EmailMultiAlternatives(subject='Stories', body=mail_text, from_email=settings.EMAIL_HOST_USER, to=email_list, )
    # msg.attach_alternative(mail_text, "text/html")
    # msg.send()



# celery -A multikart worker --beat --scheduler django --loglevel=info


# @shared_task
# def send_mail_to_subscribers():
#     # select email from Subscriber # (('idris',), ('idris'), ('idris'))
#     # email_list = Subscription.objects.filter(is_active=True).values_list('email', flat=True)
#     email_list = []
#     g = User.objects.filter(is_active=True).values_list('last_login','username', 'email')
#     for gg in g:
#         now = datetime.now(timezone.utc)
#         if (now-gg[0] > timedelta(days=30)):
#             email_list.append(gg[2])
#     products = ProductVersion.objects.annotate(num_tags=models.Count('reviews')).filter(created_at__gte=datetime.now(timezone.utc)-timedelta(days=30)).order_by('-num_tags')[:5]
    
#     mail_text = render_to_string('email-subscribers.html', {
#         'products': products, 
#     })    
#     msg = EmailMultiAlternatives(subject='Products', body=mail_text, from_email=settings.EMAIL_HOST_USER, to=email_list, )
#     msg.attach_alternative(mail_text, "text/html")
#     msg.send()
#     print(email_list)
# 1. background task
# 2. paralel
# 3. periodic task
