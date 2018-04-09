# -*- coding: utf-8 -*-
from django.shortcuts import render

def index(request):
    context ={}
    context['title'] = '你好！世界！'
    return render(request, 'bootstrap/dashboard/index.html', context)