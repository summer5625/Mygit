#路飞决定根据销售额给员工发提成，提成为阶梯制，假设一个销售人员基本工资为3000元，每月业绩低于5万元，无提成；5万至10万，提成3%；
# 10万至15万提成5%，15万-25万提成8%；25万至35万提成10%，35万以上，提成15%；从键盘获取用户当月业绩，计算其工资+提成的总额
n=int(input("当月业绩："))
if 0<=n and n<50000:
    salary=3000
    print("当月工资：",salary)
elif n<100000:
    salary=3000+n*0.03
    print("当月工资：",salary)
elif n<150000:
    salary=3000+n*0.05
    print("当月工资：",salary)
elif n<250000:
    salary=3000+n*0.08
    print("当月工资：", salary)
elif n<350000:
    salary=3000+n*0.1
    print("当月工资：",salary)
else:
    salary=3000+n*0.15
    print("当月工资：", salary)