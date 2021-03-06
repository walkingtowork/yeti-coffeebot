from .base import *
import os

DEBUG = True
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")

ALLOWED_HOSTS = [os.getenv('ALLOWED_HOST'), ]

