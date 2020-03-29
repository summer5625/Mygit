import json
import os
import sys

BAS_DIR = os.path.abspath(__file__)
BAS_DIR = os.path.dirname(os.path.dirname(BAS_DIR))
sys.path.append(BAS_DIR)                                              # 将路径添加到查找目录

from conf import setting                                              # 导入配置模块


interests = setting.TRANSACTION_TYPE                                  # 获取利息
logging_tyeps = setting.LOG_NAME                                      # 获取日志保存名称

def account_data(account_ID):

    account_path = r'%s\db\accounts\%s.json'%(BAS_DIR,account_ID)     # 获取用户数据文件路径
    f = open(account_path,'r',encoding='utf-8')
    tmp_data = f.read()
    data = json.loads(tmp_data)                                       # 获取用户的数据
    return data,account_path


aa = account_data('00001')
print(aa)