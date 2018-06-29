# -*- coding: utf-8 -*-
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

from .froms import UserForm

# 注册
@csrf_exempt
def register_view(req):
    context = {}
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            # 获得表单数据
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
    pass


# 登入
@csrf_exempt
def login_view(req):
    pass


# 登出
@csrf_exempt
def logout_view(req):
    #清理cookie里保存username
    auth.logout(req)
    return redirect('/')