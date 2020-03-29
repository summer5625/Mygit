# -*- coding: utf-8 -*-
# @Time    : 2019/10/28  17:53
# @Author  : XiaTian
# @File    : ffff.py

a = ["fa fa-address-book", "fa fa-clipboard", "fa fa-address-book-o", "fa fa-clipboard", "fa fa-address-card",
     "fa fa-clipboard", "fa fa-address-card-o", "fa fa-clipboard", "fa fa-adjust", "fa fa-clipboard",
     "fa fa-american-sign-language-interpreting", "fa fa-clipboard", "fa fa-anchor", "fa fa-clipboard", "fa fa-archive",
     "fa fa-clipboard", "fa fa-area-chart", "fa fa-clipboard", "fa fa-arrows", "fa fa-clipboard", "fa fa-arrows-h",
     "fa fa-clipboard", "fa fa-arrows-v", "fa fa-clipboard", "fa fa-asl-interpreting", "fa fa-clipboard",
     "fa fa-assistive-listening-systems", "fa fa-clipboard", "fa fa-asterisk", "fa fa-clipboard", "fa fa-at",
     "fa fa-clipboard", "fa fa-audio-description", "fa fa-clipboard", "fa fa-automobile", "fa fa-clipboard",
     "fa fa-balance-scale", "fa fa-clipboard", "fa fa-ban", "fa fa-clipboard", "fa fa-bank", "fa fa-clipboard",
     "fa fa-bar-chart", "fa fa-clipboard", "fa fa-bar-chart-o", "fa fa-clipboard", "fa fa-barcode", "fa fa-clipboard",
     "fa fa-bars", "fa fa-clipboard", "fa fa-bath", "fa fa-clipboard", "fa fa-bathtub", "fa fa-clipboard",
     "fa fa-battery", "fa fa-clipboard", "fa fa-battery-0", "fa fa-clipboard", "fa fa-battery-1", "fa fa-clipboard"]

for i in a:
     if i == 'fa fa-clipboard':
          a.remove(i)

# print(a)

# b = "fa fa-clipboard"
# c = []
# print(b.split(' '))
# for i in a:
#
#      d = i.split(' ')
#      c.append((d[0], d[1]))
# e = []
# for i in c:
#
#      str = "<i class='%s %s' aira-hidden='true'></i>" % (i[0], i[1])
#      e.append([i[1], str])
#
# print(e)

# ####################################数据构造####################################

ll = [
     {'id': 1, 'title': 456},
     {'id': 2, 'title': 123}
]

dic = {     }


for item in ll:

     dic[item['id']] = item

dic[2]['title'] = 789
# print(ll)
# print(dic)

"""

上面结果可以得出：
     在python中如果一个列表元素是字典，并将列表中的每个元素中的key和元素构造成一个新字典，那么在新字典中修改了相应key
     对应的value值后，在列表中对应的元素值也同时被修改了

"""

# ####################################end####################################

a = {'a':1, 'b':2}

b = a
c = a.copy()

a['a'] = 3
print(id(a['a']))
# print(id(b))
print(id(c['a']))
print(a)
print(b)
print(c)






