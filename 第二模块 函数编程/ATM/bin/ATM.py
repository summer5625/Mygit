from core import landing
from core import main


print('欢迎使用本行ATM！')
print('请插入卡片！')
account_ID = input('请输入卡号：').strip()         # 读取用户行用卡卡号

@landing.account_land
def operation(account_ID):
    main.function(account_ID)

operation(account_ID)
