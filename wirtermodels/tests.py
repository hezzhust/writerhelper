# -*- coding: utf-8 -*-
import os,django
from django.apps import AppConfig
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "writerhelper.settings")
django.setup()

# Create your tests here.

def saveBook():
    from models import BookInfo

    book = BookInfo (name="《三体》")
    book.save()

if __name__=="__main__":
    saveBook()