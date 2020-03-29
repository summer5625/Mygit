import accounts_data
import datetime
import landing
import logger
import json
import os


# 新用户注册

def add_account():
    new_account = input('设置用户ID:').strip()
    account_file = r'%s\db\accounts\%s.json'%(accounts_data.BAS_DIR,new_account)        # 获取新用户注册后用户信息存放路径
    if not os.path.exists(account_file):
        account_password = input('设置密码：')
        account_info = {
                        'ID':new_account,                                               # 用户ID
                        'password':account_password,                                    # 用户密码
                        'total':15000,                                                  # 用户信用额度
                        'surplus':15000,                                                # 用户可用额度
                        'pay_back':0,                                                   # 用户应还金额
                        'balance':0,                                                    # 账户余额
                        'user_locks':0,                                                 # 用户冻结状态，0位正常，1为未冻结
                        'land_status':0,                                                # 用户登录状态，0位未登录，1为登录
                        'back_day':10,                                                  # 上个月消费的免息还款日期
                        'back_statu':0                                                  # 上个月的欠款是否还清，0代表还清，其余代表未还清
        }

        f = open(account_file,'w',encoding='utf-8')
        json.dump(account_info,f)

    else:
        print('ID与他人重复！')


# 账户冻结

@landing.account_land
def frozen_account(account_ID):
    ac_data = accounts_data.account_data(account_ID)[0]
    ac_data['user_locks'] = 1                                                             # 将用户冻结状态修改为1
    ac_data['land_status'] = 0                                                            # 冻结后将用户在线状态修改为0
    lock_time = datetime.datetime.now()                                                   # 获取用户冻结时间
    lock_log = '%s %s被冻结'%(lock_time,account_ID)                                        # 记录冻结日志
    landing.save_file(ac_data,account_ID)
    trans_logger = logger.logs('landing')
    trans_logger.info(lock_log)
    print('冻结成功！')


# 用户信用额度管理

@landing.account_land
def change_credit(account_ID):
    ac_data = accounts_data.account_data(account_ID)[0]
    old_credit = ac_data['total']
    print('当前信用额度：',ac_data['total'])
    flag = True
    while flag:
        c_credit = input('请输入调整后的额度：').strip()
        if c_credit.isdigit():
            c_credit = float(c_credit)
            ac_data['total'] = c_credit
            c_credit_log = '%s  信用额度从%s修改为%s'\
                           %(account_ID,old_credit,c_credit)                              # 记录日志
            landing.save_file(ac_data, account_ID)                                        # 保存修改后数据
            trans_logger = logger.logs('tansaction')
            trans_logger.info(c_credit_log)
            print('额度修改成功！')
        elif c_credit =='b':
            flag = False
        else:
            print('请输入正确的金额！')



