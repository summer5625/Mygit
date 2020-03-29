import time
import os
import re

from core import accounts_data, logger
from core import calculator
from core import landing
from core import manage


# 查看账户信息

@landing.account_land
def view_account_info(account_ID):

    ac_data = accounts_data.account_data(account_ID)[0]
    show_info = """
    ----------用户信息----------
    总额度：     %s
    可用额度：   %s
    本月应还：   %s
    还款日：     %s
    余额：       %s
    
    """ % (ac_data['total'],
           ac_data['surplus'],
           ac_data['pay_back'],
           ac_data['back_day'],
           ac_data['balance']

           )
    print(show_info)


# 取现

@landing.account_land
def with_draw(account_ID):

    ac_data = accounts_data.account_data(account_ID)[0]
    if ac_data['back_statu'] == 0:
        flag = True
        deal_type = 'with_draw'                                                              # 获取交易方式
        while flag:
            need_money = input('请输入取现金额：').strip()
            if need_money.isdigit():
                intest = calculator.deal(deal_type, need_money, account_ID)                  # 获取取现手续费
                withdraw_log = '%s  取现：%s  手续费：%s  borrow'\
                               % (account_ID,need_money, intest)                             # 输出日志内容
                trans_logger = logger.logs('tansaction')
                trans_logger.info(withdraw_log)
            elif need_money == 'b':                                                          # 返回主菜单
                flag = False
            else:                                                                            # 判断输入金额是否合格
                print('输入金额不是整数，请重新输入！')
    else:
        print('您还有借款未还清，请还清后再交易！')


# 转账

@landing.account_land
def transfer(account_ID):

    ac_data = accounts_data.account_data(account_ID)[0]
    if ac_data['back_statu'] == 0:
        deal_type = 'transfer'
        flag = True
        while flag:
            trans_ID = input('请输入转入账户：')
            trans_file = '%s.json' % (trans_ID)
            file_path = r'%s\db\accounts\%s' % (accounts_data.BAS_DIR, trans_file)
            if os.path.exists(file_path):                                                    # 判断转入账户是否存在
                if trans_ID != account_ID:
                    trans_data = accounts_data.account_data(trans_ID)[0]                         # 获取转入账户用户数据
                    need_money = input('请输入转账金额：').strip()
                    if need_money.isdigit():
                        intest = calculator.deal(deal_type, need_money, account_ID)              # 计算转账手续费
                        trans_data['balance'] = float(need_money) + trans_data['balance']
                        calculator.save_file(trans_data, trans_ID)
                        trans_out_log = '%s  向%s转账%s  手续费：%s  borrow'\
                                        % (account_ID, trans_ID, need_money, intest)             # 记录转账日志
                        trans_in_log = '%s  %s向您的%s账户转入%s' \
                                       % (trans_ID, account_ID, trans_ID, need_money)            # 记录转账日志
                        trans_logger = logger.logs('tansaction')
                        trans_logger.info(trans_in_log)
                        trans_logger.info(trans_out_log)
                    else:
                        print('请输入正确的金额！')
                else:
                    print('不能向自己转账！')
            elif trans_ID == 'b':                                                             # 返回主菜单
                flag = False
            else:
                print('输入账号不对，请核实后再操作！')
    else:
        print('您还有借款未还清，请还清后再交易！')

# 超期未还款，锁定用户借款

@landing.account_land
def lock_borrow(account_ID):
    ac_data = accounts_data.account_data(account_ID)[0]
    shut_day = '%s'%(time.localtime().tm_mday)
    if int(shut_day) >= ac_data["back_day"]:
        ac_data[ "back_statu"] = 1
        calculator.save_file(ac_data, account_ID)


def re_back_money(account_ID):
    back_flag = True
    ac_data = accounts_data.account_data(account_ID)[0]
    should_accrual = calculator.back_money(account_ID)                            # 获取还款利息
    should_back = ac_data["pay_back"] + should_accrual                            # 计算应还金额
    print('本月应还：%s'%(should_back))
    while back_flag:
        real = input('请输入还款金额：').strip()
        if not re.findall(r'[A-Za-z]',real):                                      # 判断输入是否为数字
            real_back = float(real)
            if real_back <= should_accrual:                                       # 实际还款金额少于利息，将剩下利息计入本金中
                left_money = ac_data["pay_back"] + (should_accrual - real_back)
                ac_data["pay_back"] = left_money
                calculator.save_file(ac_data, account_ID)
                back_log = '%s  还款：%s' % (account_ID, real_back)                # 还款成功记录还款日志
                trans_logger = logger.logs('tansaction')
                trans_logger.info(back_log)
            elif real_back <= should_back:                                        # 实际还款金额小于本息和时，优先结算利息
                left_money = ac_data["pay_back"] - (real_back - should_accrual)   # 计算剩余未还本金
                ac_data["pay_back"] = left_money
                ac_data["surplus"] = 15000 - left_money                           # 计算可用额度
                calculator.save_file(ac_data, account_ID)
                back_log = '%s  还款：%s' % (account_ID, real_back)                # 还款成功记录还款日志
                trans_logger = logger.logs('tansaction')
                trans_logger.info(back_log)
            elif real_back > should_back:
                print('输入金额超出应还金额，请重新输入！')
        elif real == 'b':
            back_flag = False
        else:
            print('请输入正确的还款金额！')

# 还款

@landing.account_land
def back_money(account_ID):
    re_back_money(account_ID)
    ac_data = accounts_data.account_data(account_ID)[0]
    if ac_data["pay_back"] == 0:
        ac_data["back_statu"] = 0
        calculator.save_file(ac_data, account_ID)
    else:
        ac_data["back_statu"] = 1
        calculator.save_file(ac_data, account_ID)


# 功能分发

def function(account_ID):
    flag = True
    functions = '''
        1.信息查询         2.取款
        3.账户冻结         4.转账
        5.额度管理         6.还款
        7.账户添加         8.退出
    '''
    while flag:
        print(functions)
        func_choice = input('请选择要执行功能：').strip()
        if func_choice.isdigit():
            func_choice = int(func_choice)
            if func_choice == 1:
                view_account_info(account_ID)
            elif func_choice == 2:
                with_draw(account_ID)
            elif func_choice == 3:
                manage.frozen_account(account_ID)
            elif func_choice == 4:
                transfer(account_ID)
            elif func_choice == 5:
                manage.change_credit(account_ID)
            elif func_choice == 6:
                back_money(account_ID)
            elif func_choice == 7:
                manage.add_account()
            elif func_choice == 8:
                landing.out_land(account_ID)
                flag = False
            else:
                print('请输入正确功能序号!')






