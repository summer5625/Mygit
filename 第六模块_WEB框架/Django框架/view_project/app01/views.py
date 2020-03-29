from django.shortcuts import render, HttpResponse
import datetime

# Create your views here.


def index(request):

    return HttpResponse('OK')


def login(request):

    data = {'method': request.method, 'path': request.path, 'post_data': request.POST}

    return render(request, 'app01/login.html', {'data': data})


def model(request):

    s = '淑媛'
    i = 23
    l = ['淑媛', 23, '芳华', 23, '站站']
    kl = []
    d = {'name': '淑媛', 'age': 23}
    b = True
    class People:

        def __init__(self, name, age):
            self.name = name
            self.age = age

    p1 = People('淑媛', 23)
    p2 = People('芳华', 20)

    p_l = [p1, p2]

    now = datetime.datetime.now()
    val = 25658782
    l_str = '是否应该习惯这种淑媛，距离很近可惜关系很远，天天可却不能谈心里的感觉'
    l_e = 'I love you so much!Do you know i love you'
    bq = "<a href='#'>click</a>"

    return render(request, 'app01/models.html', locals()) #如果有多个变量需要传参，则用locals()