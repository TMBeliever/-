from django.shortcuts import render_to_response
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from getGrade import GetGrade
from django.http import HttpResponse
import json
@csrf_exempt
def test(request):
        query = request.POST.get('username', '')  # request.GET是一个类字典对象，它包含所有GET请求的参数，这里表示取得name为'q'的参数值
        password = request.POST.get('password', '')  # request.GET是一个类字典对象，它包含所有GET请求的参数，这里表示取得name为'q'的参数值
        results=None
        if query and password:
            p = GetGrade(query, password)
            if p != 1:
                results = {
                    'code':1,
                    'data':p,
                    'msg':'登录成功'
                }
            else:
                results= {
                    'code':0,

                    'msg':'用户名密码不匹配'}

        return HttpResponse(json.dumps(results))
