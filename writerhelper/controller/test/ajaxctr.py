# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.
from django.shortcuts import render_to_response
#导入render_to_response
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt

import json


names=list();
names.append("zhangsa")
names.append("aa")
names.append("b")
names.append("c")

@csrf_exempt
def aaa(request):
    name = request.POST.get("name", None)
    rtxt = ""
    code = 0
    if name is not None:
        b = name in names
    if b:
        rtxt = "名字已经存在！"
        code =101
    else:
        rtxt = "名字不存在！"
    print rtxt, code
    return HttpResponse(json.dumps({"msg":rtxt, "code":code}))