from django.shortcuts import render, HttpResponse
import json

from aj01.models import *


def index(request):

    print(request.GET.get('get'))
    return render(request, 'aj01/1、vue起步.html')


def test(request):

    n1 = int(request.POST.get('n1'))
    n2 = int(request.POST.get('n2'))
    n = n1 + n2
    print(request.POST)

    return HttpResponse(n)


def login(request):

    print(request.body)  #后获取的数据是二进制的，例如：b'{"user":"summer","pwd":"123456"}'
    data = json.loads(request.body)  #反序列化从客户端提交过来的json数据

    user = data.get('user')
    password = data.get('pwd')

    ret = {'name': None, 'msg': None}
    if User.objects.filter(user=user,password = password):

        ret['name'] = User.objects.filter(user=user).first().user

    else:

        ret['msg'] = '用户名或密码错误!'
    print(ret)
    return HttpResponse(json.dumps(ret))


def file_put(request):

    if request.method == 'POST':

        # print(request.body) #得到的是网页提交过来的请求体的原始数据
        print(request.POST) #POST只有在标签属性为enctype="application/x-www-form-urlencoded"才有值
        print(request.FILES) #获取用户上传文件内容
        file = request.FILES.get('file') #获取上传文件对象，file.name获取上传文件的名称

        with open(file.name, 'wb') as f:
            for lin in file:
                f.write(lin)
        return HttpResponse('OK')

    return render(request, 'aj01/file_put.html')
    
    

    
    
    
    
    