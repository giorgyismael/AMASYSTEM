#coding:utf-8

import django
from django.conf import settings
from django.core.mail import send_mail
settings.configure()

print(settings.EMAIL_HOST_USER)

send_mail('Subject here', 'Here is the message.', settings.EMAIL_HOST_USER,
         ['giorgyismael@gmail.com'], fail_silently=False)