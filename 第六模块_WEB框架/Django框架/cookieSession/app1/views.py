from django.shortcuts import render, HttpResponse, redirect
import datetime


from app1.models import *


def login(request):

    if request.method == 'POST':

        user = request.POST.get('user')
        pwd = request.POST.get('pwd')

        ret = User.objects.filter(name=user, password=pwd).first()

        if ret:

            date = datetime.datetime(year=2019, month=10, day=9,hour=14,minute=23)
            # response = HttpResponse('登陆成功!')
            response = redirect('/app1/index/')
            response.set_cookie('is_login', True)

            #设置cookie数据的超时时间
            # response.set_cookie('is_login', True, max_age=5)
            # response.set_cookie('username', ret.name,expires=date)

            #设置cookie数据的有效路径
            response.set_cookie('username', ret.name, path='/app1/index/')

            '''
                调用set_cookie的对象是，HttpResponse(...)，render(...)和redirect()实例化的对象
                max_age=5设置浏览器保存cookie数据时长，单位是秒
                expires是规定在哪个时间点cookie数据失效
            '''

            return response

    return render(request, 'login.html')


def index(request):

    print('浏览器发送的cookie:', request.COOKIES)

    is_login = request.COOKIES.get('is_login')

    if is_login:

        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        name = request.COOKIES.get('username')
        last_time = request.COOKIES.get('last_visit_time', '')
        print('上次登陆时间:',last_time)

        response = render(request, '1、vue起步.html', locals())
        response.set_cookie('last_visit_time', now)

        return response
    else:

        return redirect('/app1/login/')


def test(request):

    print('test:', request.COOKIES)

    return HttpResponse('test')


def session_login(request):

    if request.method == 'POST':

        user = request.POST.get('user')
        pwd = request.POST.get('pwd')

        ret = User.objects.filter(name=user, password=pwd).first()

        if ret:
            '''
            session的执行步骤：
                1、生成随机的字符串 fhghgjj456
                2、给响应体设置cookie：response.set_cookie('sessionid', fhghgjj456)
                3、在django_session表中创建一条记录：
                    session_key                 session_data
                    fhghgjj456      {'is_login': True,'username': ret.name}
            '''
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            request.session['is_login'] = True
            request.session['username'] = ret.name
            request.session['last_time'] = now
            
            return HttpResponse('登陆成功!')

    return render(request, 'login.html')


def session_index(request):
    '''
    获取django_session表中session_data值得步骤：
        1、从响应体的cookie中获取上次访问时生成的随机字符串：request.COOKIE.get('sessionid')
        2、在django_session表中过滤出session_key为request.COOKIE.get('sessionid')的记录
        3、获取记录后读取上次存储的session_data中的相应字段的值
    '''

    # print(request.session['is_login'])
    # print(request.COOKIES.get('sessionid'))

    # request.session.pop('usern') #删除session_data中的一个键值对
    print('key:',request.session.keys()) #查看用户设置的session_data中字典的键值

    # print('setdefault:',request.session.setdefault('username', 'u2')) #添加键值对

    print('items:', request.session.items())  # 获取session_data的 key-vlaue


    if request.session['is_login']:

        name = request.session['username']
        last_time = request.session['last_time']

        return render(request, '1、vue起步.html', {'name': name, 'last_time': last_time})

    return redirect('/app1/session_login/')


def logout(request):

    #del request.session['is_login'] #只能删除一个数据，不能删除对应的一条数据记录

    request.session.flush() #删除当前会话中的cookie和服务端中django_session表中对应的记录

    return redirect('/app1/session_login/')