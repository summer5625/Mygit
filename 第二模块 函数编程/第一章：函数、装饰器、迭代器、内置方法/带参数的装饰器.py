user_status = False


def login(types):
    def outer(func):
        def inner(*args,**kwargs):

            _username_ = 'alex'
            _userpassword_ = 'abc123'
            global user_status
            if user_status == False:
                username = input('users:')
                userpassword = input('password:')
                if username == _username_ and userpassword == _userpassword_:
                    print('welcom....')
                    user_status = True

                else:
                    print('wrong username or password!')
            else:
                print('用户已登录，登录验证通过...')

            if user_status  == True:
                func(*args,**kwargs)
        return  inner
    return outer

def home():
    print('---首页---')
@login('qq')
def American(types):

    print('---欧美专区---',types)
@login('weixin')
def Japan():


    print('---日韩专区---')

def zhejiang():
    print('---浙江专区---')

home()
# md=login('qq')
# print(md)
# American=md(American)
# print(American)
American('3P')
