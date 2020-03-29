#北京地铁交通价格调整为：6公里(含)内3元;6公里至12公里(含)4元;12公里至22公里(含)5元；22公里至32公里(含)6元;32公里以上部分，
# 每增加1元可乘坐20公里。使用市政交通一卡通刷卡乘坐轨道交通，每自然月内每张卡支出累计满100元以后的乘次价格给予8折优惠；
# 满150元以后的乘次给予5折优惠，假设每个月，小明都需要上20天班，每次上班需要来回1次，即每天需要乘坐2次同样路线的地铁,
# 编写程序，从键盘获取距离，帮小明计算每月的总花费。
dis=int(input("请输入乘车距离："))
n=1
if 0<=dis and dis<=6:
    price=3
    b = 100 // price + 1
    while n<=40:
        if price*n<=100:
            a=price*n
        elif price*b+price*(40-b)*0.8<=150:
            a=price*b+price*(40-b)*0.8
        else:
            a=price*b+price*(c-b)*0.8+0.5*price*(40-c)
        n += 1
    print("乘车费用：", a)
elif dis<=12:
    price=4
    b = 100 // price
    while n<=40:
        if price*n<=100:
            a=price*n
            b=n
        elif price*b+price*(40-b)*0.8<=150:
            a=price*b+price*(40-b)*0.8
            c=n
        else:
            a=price*b+price*(c-b)*0.8+0.5*price*(40-c)
        n += 1
    print("乘车费用：", a)
elif dis<=22:
    price=5
    b = 100 // price
    c = 100//price+(150-price*b)//(0.8*price)
    while n<=40:
        if price*n<=100:
            a=price*n
            b=n
        elif price*b+price*(40-b)*0.8<=150:
            a=price*b+price*(40-b)*0.8
            c=n
        else:
            a=price*b+price*(c-b)*0.8+0.5*price*(40-c)
        n += 1
    print("乘车费用：", a)
elif dis<=32:
    price=6
    b=100//price+1
    c = b + (150 - price * b) // (0.8 * price)
    while n<=40:
        if price*n<=100:
            a=price*n
        elif price*b+price*(40-b)*0.8<=150:
            a=price*b+price*(40-b)*0.8
        else:
            a=price*b+price*(c-b)*0.8+0.5*price*(40-c)
        n += 1
    print("乘车费用：", a)
else:
    price=6+(dis-32)//20
    if dis > 32:
        if (dis - 32) % 20 == 0:  # 判断超出32公里后的距离是否是20的整数倍
            price = 6 + (dis - 32) // 20
            if 100 % price == 0:  # 判断当费用累积到100时，乘坐次数是否是整数次
                b = 100 // price
            else:
                b = 100 // price + 1
            if (150 - price * b) % (0.8 * price) == 0:  # 判断当费用累积到150时，乘坐次数是否是整数次
                c = (150 - price * b) // (0.8 * price)
            else:
                c = (150 - price * b) // (0.8 * price) + 1
            print(b, c, price)
        else:
            price = 6 + (dis - 32) // 20 + 1
            if 100 % price == 0:  # 判断当费用累积到100时，乘坐次数是否是整数次
                b = 100 // price
            else:
                b = 100 // price + 1
            if (150 - price * b) % (0.8 * price) == 0:  # 判断当费用累积到150时，乘坐次数是否是整数次
                c = (150 - price * b) // (0.8 * price)
            else:
                c = (150 - price * b) // (0.8 * price) + 1
            print(b, c, price)
    while n<=40:
        if price *n <= 100:
             a = price * n
        elif price * b + price * (40-b) * 0.8 <= 150:
             a = price * b + price * (40-b) * 0.8
        else:
             a = price * b + price * (c-b) * 0.8 + 0.5 * price * (40-c)
        n += 1
    print("乘车费用：", a)