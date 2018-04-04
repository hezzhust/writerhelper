# -*- coding: utf-8 -*-
from django.shortcuts import render

def hello(request):
    context ={}
    context['hello'] = 'hello hezz good job! 贺政忠 干得漂亮！'
    return render(request, 'hellow.html', context)