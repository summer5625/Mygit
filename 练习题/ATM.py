from collections import Counter

statu = False

# 新用户注册

def add_user():
    data = msg_load()
    account_name = input('请设置用户名：').strip()
    account_password = input('请设置用户密码：').strip()
    if account_name:
        if account_name not in data['user_names']:
            data['user_names'].append(account_name)
            data['user_passwords'].append(account_password)
            data['user_locks'].append('open')
        else:
            print('用户名重复，请重新输入！')
    else:
        print('用户名不能为空！')


# 加载用户信息

def msg_load():
    user_data = {
        'user_names':[],                    # 用户名
        'user_passwords':[],                # 用密码
        'user_locks':[],                    # 用户冻结状态
        'land_status':[],                   # 用户登录状态
        'total':[],                         # 信用总额度
        'surplus':[],                       # 可用额度
        'pay_back':[],                      # 应还金额
        'balance':[]                        # 用户余额（不能小于0）

    }
    f = open('用户信息.db','r',encoding = 'utf-8')
    for lin in f:
        user_name,user_password,user_lock,land_statu,tatal,surplus,pay_backs,balance = lin.strip().split(',')
        user_data['user_names'].append(user_name)
        user_data['user_passwords'].append(user_password)
        user_data['user_locks'].append(user_lock)
        user_data['land_status'].append(land_statu)
        user_data['total'].append(tatal)
        user_data['surplus'].append(surplus)
        user_data['pay_back'].append(pay_backs)
        user_data['balance'].append(balance)


    f.close()
    return  user_data

# 用户认证
def user_land(func):
    def user_inner():
        data = msg_load()
        count = 0
        mis_name = []                                                # 创建一个空列表来记录输入错误密码的用户名，每次重启程序清空
        global statu
        if statu == False:                                           # 用户登录状态检测
            while count < 5:
                name = input('用户名：').strip()
                if name in data['user_names']:                       # 判断用户是否注册
                    sn = data['user_names'].index(name)
                    if data['user_locks'][sn] == 'open':             # 检测用户是否被冻结
                        password = input('登录密码：').strip()
                        if password == data['user_passwords'][sn]:
                            statu = True                             # 登录成功则修改用户登录状态
                            data['land_status'][sn] = 'live'
                            print('登录成功！')
                            break
                        else:
                            print('账号或者密码错误！')
                            count += 1
                            mis_name.append(name)                    # 将输入错误密码的账号存入列表中
                            lock_names = dict(Counter(mis_name))     # 将账号输错密码的次数统计出来
                            for i in lock_names:                     # 判断同一个账户是否密码输入次数超过三次，超过三次则冻结
                                if lock_names[i] == 3:
                                    n = data['user_names'].index(i)
                                    data['user_locks'][n] = 'lock'
                                    print('%s用户密码输入次数过多，账户被冻结，请前往柜台解冻！' % (i))
                                    print(data['user_locks'])
                    else:
                        print('%s账号被冻结！' % (name))              # 冻结账号不计入输入次数
                else:
                    print('用户未注册！请注册后再登录')
                    add_user()
                    count += 1
                if count == 5:                                       # 每日最多尝试输入五次错误的账号或者密码
                    print('今日输入错误次数超过5次，请明天再试！')
        else:
            print('用户已登录，登录验证通过...')

        if statu == True:
            func()



    return user_inner


# 账号登录状态检测

def check_statu():
    data = msg_load()
    if 'live' in data['land_status']:                  # 判断用户是否在线，在线则获取在线用户的用户名和序列号
        sn = data['land_status'].index('live')
    return sn


# 退出登录,切换用户
@user_land
def out_land():
    global statu
    data = msg_load()
    sn = check_statu()                                # 获取在线用户的序列号
    data['land_status'][sn] = 'death'                 # 退出登录时将用户在线状态修改
    statu = False                                     # 退出登录时将用户登录态修改
    print('已退出')
    return statu

# 查看账户信息

@user_land
def view_account_info():
    sn = check_statu()                                # 获取在线用户的序列号
    data = msg_load()                                 # 加载用户信息
    print('余额：',data['balance'][sn])
    print('总额度：',data['total'][sn])
    print('可用额度：',data['surplus'][sn])
    print('剩余应还：',data['pay_back'][sn])



# 取现
@user_land
def with_draw():
    sn = check_statu()
    data = msg_load()
    can_cash = int(data['surplus'][sn])                                               # 剩余信用额度
    c_balance = int(data['balance'][sn])                                              # 剩余可用金额
    flag = True
    print('优先使用余额取现，余额不足时使用信用额度补足！')
    print('可提现金额：',can_cash)
    while flag:
        cash = input('请输入取现金额：').strip()
        if cash != 'q':                                                                # 返回主菜单
            if cash.isdigit():
                cash = int(cash)
                if (can_cash + c_balance) >= (cash*0.05+cash):                                     # 余额不足，无法取现
                    if (cash*0.05+cash) <= c_balance:                                              # 优先使用余额取现
                        data['balance'][sn] = c_balance - (cash*0.05+cash)                         # 求出余额
                        print('取现成功！')
                        break
                    else:                                                              # 余额不足，使用信用额度补足
                        data['balance'][sn] = 0                                        # 将余额置0
                        l_cash = can_cash + c_balance - (cash*0.05+cash)                           # 求出可用信用额度
                        data['surplus'][sn] = l_cash
                        data['pay_back'][sn] = int(data['total'][sn]) - l_cash         # 求出要还的金额
                        print('取现成功！')
                        break
                else:
                    print('余额不足！')

            else:
                print('请输入正确的金额！')
        else:
            flag = False


# 转账
@user_land
def transfer():
    flag = True
    data = msg_load()
    sn = check_statu()
    can_transfer = int(data['surplus'][sn])                                            # 剩余信用额度
    can_balance = int(data['balance'][sn])                                             # 剩余额度
    while flag:
        print('可用额度：', data['surplus'][sn])
        t_name = input('请输入要转入的账号：').strip()
        if t_name != 'q':
            if t_name in data['user_names']:                                           #检测转入账户是否存在，只支持同行转账
                t_cash = input('请输入转账金额：').strip()
                t_sn = data['user_names'].index(t_name)
                if t_cash.isdigit():
                    t_cash = int(t_cash)
                    if (can_transfer + can_balance) >= t_cash:                         # 余额不足，无法转账
                        if t_cash <= can_balance:                                      # 优先使用余额转账
                            data['balance'][sn] = can_balance - t_cash                 # 求出余额
                            data['balance'][t_sn] = t_cash                             # 将转入金额，存入转入用户余额中
                            print('转账成功！')
                            print(data)
                            break
                        else:                                                          # 余额不足，使用信用额度补足
                            data['balance'][sn] = 0                                    # 将余额置0
                            l_cash = can_transfer + can_balance - t_cash               # 求出可用信用额度
                            data['surplus'][sn] = l_cash
                            data['pay_back'][sn] = int(data['total'][sn]) - l_cash     # 求出要还的金额
                            data['balance'][t_sn] = t_cash                             # 将转入金额，存入转入用户余额中
                            print('转账成功！')
                            print(data)
                            break
                    else:
                        print('余额不足！')

                else:
                    print('请输入正确的金额！')
            else:
                print('用户不存在，请核实账户后再转账！')
        else:
            flag = False                                                               # 返回主菜单


# 还款
@user_land
def be_pay_back():
    data = msg_load()
    sn = check_statu()
    should_back = data['pay_back'][sn]
    print('应还金额：',should_back)
    flag = True
    while flag:
        r_back = input('请输入要还的金额：').strip()
        if r_back != 'q':
            if r_back.isdigit():
                r_back = int(r_back)
                if r_back <= should_back:
                    data['pay_back'][sn] = should_back -r_back
                    data

