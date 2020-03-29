import json
import logger
import accounts_data


# 保存用户数据

def save_file(ac_data,account_ID):
    ac_path = accounts_data.account_data(account_ID)[1]                    # 获取用户数据存储路径
    f = open(ac_path,'w',encoding='utf-8')
    json.dump(ac_data, f)
    f.close()

# 用户认证

def account_land(func):

    def account_inner(account_ID):
        count = 0
        ac_data = accounts_data.account_data(account_ID)[0]                # 读取用户数据
        while count<3:
            if ac_data['user_locks'] == 0:                                 # 判断用户是否被冻结，0表示未冻结，1表示冻结
                if ac_data['land_status'] == 0:                            # 判断用户认证状态，0代表未认证，1代表已认证
                    account_password = input('请输入密码：').strip()
                    if account_password == ac_data['password']:
                        ac_data['land_status'] = 1                         # 登录成功将认证状态改为1
                        save_file(ac_data,account_ID)                      # 将用户数据写入文件
                        land_log = '%s  认证成功！'%(account_ID)            # 保存登录日志
                        trans_logger = logger.logs('landing')
                        trans_logger.info(land_log)
                        print('登录成功，欢迎.....')
                    else:
                        count += 1
                        print('密码错误，请重新输入！')
                else:
                    print('登录验证通过...')
                    break
            else:
                ac_data['user_locks'] = 1                                  # 将用户冻结状态修改为1
                save_file(ac_data, account_ID)                             # 保存用户修改后数据

                print('用户已被冻结，请前往柜台解冻！')
                break
        if count == 3:                                                     # 密码输入错误超过三次，账号冻结
            ac_data['user_locks'] = 1
            save_file(ac_data,account_ID)
            frozed_log = '%s 密码输入次数过多，账户被冻结！' \
                         % (account_ID)                                   # 记录账户被冻结日志
            trans_logger = logger.logs('landing')
            trans_logger.info(frozed_log)
            print('密码输入次数过多，账号被冻结！')
        if ac_data['land_status'] == 1:
            func(account_ID)

    return account_inner

# 退出登录

@account_land
def out_land(account_ID):
    ac_data = accounts_data.account_data(account_ID)[0]
    ac_data['land_status'] = 0                                           # 退出时将登录状态置0
    save_file(ac_data,account_ID)
    out_log = '%s  退出！'%(account_ID)                                   # 记录退出登录日志
    trans_logger = logger.logs('landing')
    trans_logger.info(out_log)





