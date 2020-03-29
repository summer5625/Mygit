s='alrx'
b=list(s)
print(b)
c=tuple(s)
print(c)
# li=['alex','seven']
# d=tuple(li)
# print(d)
tu=('Alex','seven')
e=list(tu)
print(e)
#将列表转换成字典
li=['alex', 'seven']
r=dict(zip([i for i in range(10,len(li)+11)],li))
print(r)
