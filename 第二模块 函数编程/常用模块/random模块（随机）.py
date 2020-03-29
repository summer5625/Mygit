import random
import string

#取1-100间的随机数，包含100

a = random.randint(1,100)
# print(a)
# print(random.randint(1,100))

#取1-100间的随机数，不包含100

b = random.randrange(1,100)
# print(b)

#从字符串里随意返回一个字符

c = random.choice('adjhfnbxh12wyt')
# print(c)
# print(random.choice('adjhfnbxh12wyt'))


#从字符串里随意返回指定数量的字符,以列表方式返回

d = random.sample('adjhfnbxh12wyt',3)

# print(random.sample('adjhfnbxh12wyt',3))
# print(random.sample('adjhfnbxh12wyt',2))


#生成随机验证码

s = string.ascii_lowercase + string.digits  #生成小写字母和数字组合的字符串
print(s)

''.join(random.sample(s,6))                 #生成6位随机验证码
print(''.join(random.sample(s,6)) )
print(''.join(random.sample(s,6)) )
print(''.join(random.sample(s,6)) )


#洗牌，输出列表

x = list(range(20))
print(x)

random.shuffle(x)

print(x)