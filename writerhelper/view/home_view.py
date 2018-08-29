# -*- coding: utf-8 -*-

from django.shortcuts import render


def index(request):
    context ={}
    context['title'] = '首页'
    context['section_title'] = '欢迎使用写作助手！'
    return render(request, 'home.html', context)