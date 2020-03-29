import re
# f = open('嫩模联系方式.txt','r',encoding='utf-8')
# data = f.read()
#
# print(re.findall('1[0-9]{10}',data))


# a = '4acb22gf4d5g6h8t2'
# b = re.match('[0-9]',a)   #返回的是对象
# if b:                     #判断匹配到的结果是否为空，部位空则取出匹配到的值
#     print(b.group())
# re.search('[0-9]',a)
# print(re.findall('[0-9]',a))
#
# print(re.search('..',a))
#
# print(re.search('^4ac',a))   #匹配开头
#
# print(re.search('t2$',a))    #匹配结尾
#
# print(re.search('4ac*',a))
#
# print(re.search('.2.+',a))

# print(re.search('b*.{3}',a))
#
# print(re.search('2{1,3}',a))
#
# print(re.search('[a|A]lex','alex'))
#
# print(re.search('([a-z]+)([0-9]+)','alex123').groups())   #将字母和数字分开

# print(re.search('\d+','ad45c5d'))
# print(re.search('\w+','ad45c5d'))


s='411251199105163015'
b = re.search('(?P<province>\d{3})(?P<city>\d{3})(?P<born_year>\d{4})',s)
# print(b)
# print(b.groups())
# print(b.groupdict())

c = 'aa12bb33dd55#ffg-df|dX32fd'
# print(re.split('\d+|#|-|\|',c))     #\|将|的语法转换成字符|

print(re.sub('\d+','_',c,count=2))

# print(re.fullmatch('\w+@\w+\.(com|cn|edu)',"alex@oldboyedu.cn"))