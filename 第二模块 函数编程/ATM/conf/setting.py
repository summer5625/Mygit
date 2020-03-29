import os
import logging

FILE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))     # 获取程序所在文件夹的绝对路径
print(FILE_PATH)
LOG_LEVEL = logging.INFO                                                    # 设置日志的级别

LOG_NAME = {
            'tansaction':'transaction.log',                                 # 生成交易记录日志名称
            'landing':'landing.log'                                         # 登录记录日志名称
            }


TRANSACTION_TYPE = {
                     'with_draw':0.05,                                      # 设置取现的手续费
                     'transfer':0.05,                                       # 设置转账的手续费
                     'pay_back':0.04,                                       # 设置借款利率
                     'shopping':0                                           # 购物
                   }

