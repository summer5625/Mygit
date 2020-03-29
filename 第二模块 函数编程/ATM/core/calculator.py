import accounts_data
import datetime
import json
import time
import re
import os


# 保存用户数据

def save_file(ac_data,account_ID):
    ac_path = accounts_data.account_data(account_ID)[1]                            # 获取用户数据存储路径
    f = open(ac_path,'w',encoding='utf-8')
    json.dump(ac_data, f)
    f.close()

# 转账，取现，购物手续费计算

def deal(deal_type,need_money,account_ID):
    need_money = float(need_money)
    rate = accounts_data.interests[deal_type]                                      # 获取用户当前交易的利率
    ac_data = accounts_data.account_data(account_ID)[0]                            # 获取用户数据
    if  (need_money*rate+need_money) <= (ac_data['surplus']+ac_data['balance']):   # 余额不足无法交易
        if (need_money*rate + need_money) <= ac_data['balance']:                   # 优先使用余额交易
            ac_data['balance'] = ac_data['balance'] - \
                                 (need_money*rate + need_money)                    # 求出余额
            save_file(ac_data,account_ID)                                          # 保存用户数据
            interst = need_money*rate
            print('交易成功！')
            return interst
        else:                                                                      # 余额不足，使用信用额度补足
            ac_data['surplus'] = ac_data['surplus'] + \
                                 ac_data['balance'] - \
                                 (need_money*rate + need_money)                    # 求出可用信用额度
            ac_data['pay_back'] = ac_data['total'] - ac_data['surplus']            # 求出要还的金额
            ac_data['balance'] = 0                                                 # 将余额置0
            save_file(ac_data,account_ID)                                          # 保存用户数据
            interst = need_money * rate
            print('交易成功！')
            return interst

    else:
        print('余额不足！')


# 获取最后借款日期

def get_borrow_day(account_ID):
    log_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = r'%s\log\transaction.log'%(log_path)
    f = open(path, 'r', encoding='utf-8')
    b_time_list = []
    for line in f.readlines():
        a = re.findall('borrow',line)
        b = re.findall(account_ID,line)
        if a and account_ID in b:
            broow_time = re.findall('\w+-\w+-\w.',line)                            # 获取借款时间
            broow_day = time.strptime(broow_time[0],'%Y-%m-%d')                    # 将获取到的时间字符串转换成时间
            days = time.mktime(broow_day)
            b_time_list.append(days)
    b_day = max(b_time_list)                                                       # 获取最后借款时间
    return b_day

# 计算还款金额

def back_money(account_ID):
    rate = accounts_data.interests['pay_back']                                     # 获取借款利率
    ac_data = accounts_data.account_data(account_ID)[0]
    now = time.localtime(time.time())                                              # 获取还款日期
    old_time = get_borrow_day(account_ID)                                          # 获取最后借款日期
    old_day = time.localtime(old_time)                                             # 将借款日期转换成时间戳
    now_day = time.strftime('%Y-%m-%d',now)                                        # 将时间戳转换成日期格式字符串
    back_day = time.strftime('%Y-%m-10',old_day)                                   # 获取利息计算开始日期
    accrual = 0
    if time.mktime(now) > time.mktime(time.strptime(back_day,'%Y-%m-%d')):         # 判断还款时间是否超期
        last_days = (datetime.datetime.strptime(now_day, '%Y-%m-%d') -
                     datetime.datetime.strptime(back_day,'%Y-%m-%d')).days         # 计算还款超期天数
        accrual = ac_data["pay_back"] * rate * last_days                           # 计算利息
    return accrual




