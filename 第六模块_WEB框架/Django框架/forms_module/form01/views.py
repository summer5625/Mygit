from django.shortcuts import render, HttpResponse
from django.forms import widgets
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError
from django import forms  #导入form控件


from form01.models import *


#创建表单验证类
class UserForm(forms.Form):
    '''
    error_messages错误信息提示，字典形式，字典键值不能自己随意命名，要用给定的错误关键字
    widget=widgets.PasswordInput()改变input标签的type属性为password
    widget=widgets.TextInput(attrs={'class': 'active'})给标签添加属性，属性名称和值按照字典形式填写
    '''

    user = forms.CharField(min_length=5, label='用户名', error_messages={'required': '该字段不能为空', 'invalid': '长度不够，至少5个字符'}, widget=widgets.TextInput(attrs={'class': "form-control"}))
    pwd = forms.CharField(label='密码', error_messages={'required': '该字段不能为空'}, widget=widgets.PasswordInput(attrs={'class': "form-control"}))
    r_pwd = forms.CharField(label='确认密码', error_messages={'required': '该字段不能为空'}, widget=widgets.TextInput(attrs={'class': "form-control"}))
    email = forms.EmailField(label='邮箱', error_messages={'required': '该字段不能为空', 'invalid': '邮箱格式错误'}, widget=widgets.TextInput(attrs={'class': "form-control"}))
    tel = forms.CharField(label='电话', error_messages={'required': '该字段不能为空'}, widget=widgets.TextInput(attrs={'class': "form-control"}))


    def clean_user(self):
        '''
        局部钩子
        :return:
        '''

        val = self.cleaned_data.get('user')

        ret = Userinfo.objects.filter(name=val)

        if not ret:

            return val
        else:

            raise ValidationError('用户名已被注册!')

    def clean_tel(self):
        '''
        局部钩子
        :return:
        '''

        tel = self.cleaned_data.get('tel')

        if len(tel) == 11:
            return tel
        else:
            raise ValidationError('手机号码格式错误!')

    def clean(self):
        '''
        全局钩子
        :return:
        '''

        pwd = self.cleaned_data.get('pwd')
        r_pwd = self.cleaned_data.get('r_pwd')

        
        if pwd and r_pwd:
            if pwd == r_pwd:

                return self.cleaned_data
            else:

                raise ValidationError('两次密码不一致!')
        else:

            return self.cleaned_data
        
    
def register(request):

    if request.method == 'POST':

        # form = UserForm({'user': 'summer', 'pwd': '123456'}) #字典的键值必须和上面的表单验证类变量名称相同，字典的键值对个数不能少于类中变量个数
        #可以多，多出的键值对不做校验
        # print(form.is_valid())  #校验用户发过来的数据是否符合要求，返回值是布尔值，全部符合返回true

        form = UserForm(request.POST) #form表单的name属性值要与form组件字段值对应

        if form.is_valid():
            print('全部匹配成功:', form.cleaned_data) #所有字段校验成功返回校验的值
        else:
            print("匹配上的信息:", form.cleaned_data) #只返回能匹配上的项
            print("匹配出错信息:", form.errors)  #返回一个字典{'user':[]}，键值是出错的form表单提交过来的出错键值，键值是错误信息的一个列表
            print('出错信息类型:',type(form.errors))
            # print("返回错误:", form.errors['email'][0]) #一般取错误列表第一个值
            # print("错误值得类型:",type(form.errors.get("user")))


            #全局钩子错误信息
            errors = form.errors.get('__all__')
            print(errors[0])

            return render(request, 'register.html', locals())
    
    form = UserForm()

    return render(request, 'register.html', locals())


def login(request):


    return render(request, 'login.html')