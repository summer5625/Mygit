from django.shortcuts import render, HttpResponse, redirect
from django.contrib import auth
from django.contrib.auth.models import User #User相当于表中的auth_user表
from django.contrib.auth.decorators import login_required  #导入用户认证装饰器


from author1.models import *
from author_modles import settings


def login(request):

    if request.method == 'POST':
        username = request.POST.get('user')
        pwd = request.POST.get('pwd')

        user = auth.authenticate(username=username, password=pwd)

        if user: #登陆成功返回user对象，否则返回None

            auth.login(request, user)  #得到request.user:当前登录对象

            next_url = request.POST.get('next', '/author/index/')

            return redirect(next_url)

    return render(request, 'login.html')


@login_required
def index(request):
    # print(request.user)
    # print(request.user.id)  #如果没有记录则返回None
    # print(request.user.username) #如果没有记录则返回None
    # print(request.user.is_anonymous) #如果没有记录则返回True
    # # print(request.user.date_joined)
    # print(request.user.is_authenticated)
    #
    if request.user.is_anonymous:

        # return redirect('/author/login')

        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

    return render(request, '1、vue起步.html')


def logout(request):

    auth.logout(request)

    return redirect('/author/login')


def reg(request):

    if request.method == 'POST':

        username = request.POST.get('user')
        pwd = request.POST.get('pwd')
        email = request.POST.get('email')

        user = User.objects.create_user(username=username, password=pwd, email=email)

        return redirect('/author/login')

    return render(request, 'register.html')


@login_required
def test(request):

    return render(request, '1、vue起步.html')
