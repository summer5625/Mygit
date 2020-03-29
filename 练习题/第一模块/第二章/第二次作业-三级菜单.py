#! -*- coding:utf-8 -*-
menu={
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{},
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '通天苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            '人民广场':{
                '炸鸡店':{}
            },
        },
        '闸北':{
            '火车站':{
                '携程':{}
            },
        },
        '浦东':{},
    },
    '山东':{},
}

#精妙方法
link=menu
remember=[]
while True:
    for k in link:       #打印当前所在的级数菜单
        print(k)
    print('输入b返回上一级')
    print('输入q退出')
    address=input('请输入要查找地址：')
    if address in link:  #每循环一次link向下走一级
        remember.append(link)
        link = link[address]
    elif address=='b':
        link=remember.pop()
        print(link)
    elif address=='q' :
        break


#垃圾方法

# while True:
#     for k in menu:
#         print(k)
#     address=input('请输入地址：')
#     if address in menu:
#         while True: #进入第二级
#              for k in menu[address]:
#                 print(k)
#              print('输入b返回上一级')
#              print('输入q退出')
#              address2 = input('请输入地址：')
#              if address2 in menu[address]:
#                  while True:#进入第三级
#                     for k in menu[address][address2]:
#                         print(k)
#                     print('输入b返回上一级')
#                     print('输入q退出')
#                     address3 = input('请输入地址：')
#                     if address3 in menu[address][address2]:
#                          print(menu[address][address2][address3])
#                     elif address3 == 'b':
#                          break
#                     elif address3 == 'q':
#                         exit()
#                     else:
#                          print('所找地址不存在！')
#              elif  address2=='b':
#                  break
#              elif  address2=='q':
#                  exit()
#              else:
#                  print('所找地址不存在！')
#     elif address == 'q':
#         exit()