# a='大家好我是{0}，来自{1}'
# b=a.format("夏云翔","河南")
# print(a.format("夏云翔","河南"))
# print(b)
#输出结果为：大家好我是夏云翔，来自河南
# a="abcgdh"
# b="123456"   #要和a串的字符个数相同
# c=str.maketrans(a,b)
# print(c)
# #c打印出来结果为：{97: 49, 98: 50, 99: 51, 103: 52, 100: 53, 104: 54} 即将a中的字符与b中字符按顺序对应起来
# e="dceifbclawac"
# f=e.translate(c)
# print(f)
# #打印结果为：53eif23l1w13
# #即将e中的字符按照a和b中的对应关系翻译过来

# a="sssddfrefgh"
# print(a.replace('f','-'))
# #输出结果为：sssdd-refgh

# a='hello world'
# b=a.split()
# c=a.split('o')
# print(b)
# print(c)
# #结果为：['hello', 'world']
# #       ['hell', ' w', 'rld']
# a='hello world'
# print(a.startswith('he') )
# # 输出结果为：True
# print(a.count('l'))
# print(a.center(30,'-')  )






a=[1,2,3]
print(a.append(5))
a.append(5)
print(a)

