from collections import Counter
a = ['a','b','c','a','c','d','a',]


c = dict(Counter(a))

print(c)
print(c['a'],type(c['a']))
for i in c:
    # print(c[i])
    if c[i] == 3:
        print(i,c[i])