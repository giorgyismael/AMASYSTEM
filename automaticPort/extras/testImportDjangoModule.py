#coding:utf-8

import os
import sys
import django

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(BASE_DIR)
# os.environ['DJANGO_SETTINGS_MODULE'] = 'internetOfThings.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'internetOfThings.settings')
django.setup()