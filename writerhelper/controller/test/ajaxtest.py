# -*- coding: utf-8 -*-
from django.shortcuts import render

def main(request):
    context ={}
    context['title'] = '测试名称是否可用！'
    return render(request, 'ajaxtest.html', context)