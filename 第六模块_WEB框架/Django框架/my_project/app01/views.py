from django.shortcuts import render, HttpResponse #导入HttpResponse模块,响应对象
import time
from django.urls import reverse


# Create your views here.

def timer(request):

    print('参数啊',request)

    rek = time.time()
    data =time.localtime(rek)
    ctime = time.strftime('%Y-%m-%d %H:%M:%S',data)

    return render(request, 'timer.html', {'ctime': ctime})
    #render()封装了渲染网页的方法函数，里面需要两个参数:第一个默认的request和要渲染html文件,向网页传需要的参数时用字典形式传参数，相应
    #的在相应的html中的需要参数位置要填上传参数的字典的key值


def login(request):
    #查看请求方式
    # print(request.method)

    #是get请求则返回登录页面
    if request.method == 'GET':
        return render(request, 'login.html')

    else:
        #获取用户提交的信息
        print(request.POST) # <QueryDict: {'user': ['summer'], 'pwd': ['123']}>

        user = request.POST.get('user')
        pwd = request.POST.get('pwd')

        if user == 'summer' and pwd == '123':
            return HttpResponse('Success')
        else:
            return HttpResponse('Wrong username and password')




def article_2003(request):

    url = reverse('a_2003') #/app01/articles/2003/
    print(url)
    url2 = reverse('v_a_2005', args=(2005,)) #/app01/articles/2005/
    print(url2)

    return HttpResponse('article_3002') #HttpResponse()是响应对象，用于渲染着页面的


def articles_year(request, year):

    return HttpResponse('article_%s'%year)


def articles_active(request, year,month):

    return HttpResponse('artical_%s-%s'%(year,month))


def articles_detials(request, y, m, id):


    return HttpResponse('articales_%s-%s-%s'%(y,m,id))



def index(request):
    # data = '站站'

    # return HttpResponse('appo1:%s'%reverse('app01:index'))
    return HttpResponse(reverse('app01:index'))


def article_path(request, year, month):
    print(type(year))
    print(type(month))

    return HttpResponse('year:%s  month:%s' % (year, month))


def sel_url(request, month):

    return HttpResponse('type:%s  month:%s' % (type(month), month))


def change(request, number):

    re_url = reverse('change', args=(number,))
    print(re_url)
    ls = [2000, 2001, 2012]

    return render(request, 'login.html', {'ls': ls})