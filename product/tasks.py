import time
from celery import shared_task
from django.template.loader import render_to_string

from accounts.models import User

# from product.models import 

@shared_task
def process_func():
 time.sleep(10)
 return 'Proces done'



# @shared_task
# def send_mail_to_subscribers():
#  email_list = []
#  email_list = User.objects.filter(is_active=True).values_list('email',flat=True)
#  mail_text = render_to_string('email-subscribers.html', {
#         'products': products, 
#     })
#  # user_30_days_ago = 
#  # products = 



