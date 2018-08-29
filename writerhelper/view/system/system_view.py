# -*- coding: utf-8 -*-
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

from .froms import UserForm

home_path = "home.html"
register_path = "system/register.html"
login_path = "system/login.html"

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
            password_check = form.cleaned_data['password_check']
            email = form.cleaned_data['email']
            context['username'] = username
            #判断密码是否一致
            if password != password_check:
                context['passwordDifference'] = True
                return render(req, register_path, context)

            # 判断用户是否存在
            user = auth.authenticate(username=username, password=password)
            if user:
                context['userExit'] = True
                return render(req, register_path, context)
            # 添加到数据库（还可以加一些字段的处理）
            user = User.objects.create_user(username=username, password=password, email = email)
            user.save()

            # 添加到session
            req.session['username'] = username  # 调用auth登录
            auth.login(req, user)
            # 重定向到首页
            return redirect('/')

    else:
        context = {'isLogin': False}
        context['passwordDifference'] = False
    # 将req 、页面 、以及context{}（要传入html文件中的内容包含在字典里）返回
    return render(req, register_path, context)
# 登入
@csrf_exempt
def login_view(req):
    context = {}
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            # 获得表单数据
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # 获取的表单数据与数据库进行比较
            user = authenticate(username=username, password=password)
            if user:
                # 比较成功，跳转index
                auth.login(req, user)
                req.session['username'] = username
                return redirect(home_path)
            else:
                # 比较失败，还在login
                context = {'isLogin': False, 'pawd': False}
                return render(req, login_path, context)
    else:
        context = {'isLogin': False, 'pswd': True}
    return render(req, login_path, context)


# 登出
@csrf_exempt
def logout_view(req):
    # 清理cookie里保存username
    auth.logout(req)
    return redirect('/')
