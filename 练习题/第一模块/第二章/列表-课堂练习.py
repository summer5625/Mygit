#! -*- coding:utf-8 -*-
# names=['old_driver','rain','jack','shanshan','peiqi','black_gril']
# names.insert(5,"alex'")
# print(names)
# names[3]="姗姗"
# print(names)
# b=['oldboy','oldgril']
# names.insert(2,b)
# print(names)
# c=names.index('peiqi')
# print(c)
# e=[1,2,3,4,2,5,6,2]
# names.extend(e)
# print(names)
# print(names[4:7])
# print(names[2:10:2])
# print(names[-3:])

#打印列表中每个元素和其索引值
# names=['old_driver', 'rain', 'oldboy', 'oldgril', 'jack', '姗姗', 'peiqi', "alex", 'black_gril', 1, 2, 3, 4, 2, 5, 6, 2]
# for a in enumerate(names):   #enumerate枚举列表中的元素，和其索引值
#     print(a)

#打印列表中每个元素和其索引值,并将索引值为偶数的元素改为-1
# count=0
# names=['old_driver', 'rain', 'oldboy', 'oldgril', 'jack', '姗姗', 'peiqi', "alex", 'black_gril', 1, 2, 3, 4, 2, 5, 6, 2]
# # for a in enumerate(names):   #enumerate枚举列表中的元素，和其索引值
# for i in names:
#     count+=1
#     if count%2==0:
#         names[count]=-1
#     print(count,i)


#返回第二个2的索引值
# names=['old_driver', 'rain', 'oldboy', 'oldgril', 'jack', '姗姗', 'peiqi', "alex", 'black_gril', 1, 2, 3, 4, 2, 5, 6, 2]
# a=names.index(2)
# c=names[(a+1):]
# print(a+1+c.index(2))

#打印商品列表
# count=0
# products=[['iphon8',6888],['MacPro',14800],['小米6',2499],['Coffee',31],['Book',80],['Nike Shoes',799]]
# print("-------商品列表-------")
# for f,a in products:
#     print(count,f,a)
#     count+=1

#问用户要买什么？输入编号后，将商品添加到购物车，输入p后输出购物车中商品

products=[['iphon8',6888],['MacPro',14800],['小米6',2499],['Coffee',31],['Book',80],['Nike Shoes',799]]
shopping_cart=[]
run_flag=True
while run_flag:
    print("-------商品列表-------")
    for index,a in enumerate(products):
        print(index,a[0],a[1])
    choice=input("请输入要购买的商品编号：")
    if choice.isdigit():
        choice=int(choice)
        if len(products)>choice and choice>0:
            shopping_cart.append(products[choice])
            print(products[choice],"已加入购物车！")
        else:
            print("无此商品，请重新选择商品！")
    elif choice=='q':
        if len(shopping_cart)>0:
            print("------以下商品已加入购物车------")
            for a,b in  shopping_cart:
                print("%s  %s "%(a,b))
        run_flag=False
