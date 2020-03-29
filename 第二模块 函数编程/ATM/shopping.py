from core import calculator
from core import landing
from core import logger


goods=[{'name':'电脑','price':1999},
       {'name':'鼠标','price':10},
       {'name':'游艇','price':20},
       {'name':'美女','price':998}
       ]


def goods_list():
    number = 0
    print("-------商品列表-------")
    for i in goods:                                                           # 打印商品列表
        print(number, i['name'], i['price'])
        number += 1


# 添加商品到购物车

def shopping_cart():
    cart = {}                                                                 # 空购物车
    goods_list()
    flag = True
    while flag:
        choice = input("请输入要购买的商品编号：")
        if choice.isdigit():                                                  # 判断用户输入的是不是数字字符，是则将其转换成整数
            choice = int(choice)
            if 0 <= len(goods) > choice:
                good_name = goods[choice]['name']
                good_price = goods[choice]['price']
                cart[good_name] = good_price
                print('%s已加入购物车！'%(good_name))
            else:
                print('无此商品！')
        elif choice =='p':                                                    # 选择支付功能
            for k, v in cart.items():
                print(k, v)
            flag = False
        else:
            print('请输入正确的商品编号！')
    account_ID = input('请输入账号：').strip()
    @landing.account_land
    def payment(account_ID):
        deal_type = 'shopping'
        pay_money = 0
        for key in cart:
            pay_money = pay_money + cart[key]                                 # 计算付款金额
        calculator.deal(deal_type, pay_money, account_ID)                     # 购买商品付款
        landing.out_land(account_ID)                                          # 支付完成退出登录
        shopping_log = '%s  shopping  %s  borrow' % (account_ID, pay_money)
        trans_logger = logger.logs('tansaction')
        trans_logger.info(shopping_log)
    return payment(account_ID)



shopping_cart()


