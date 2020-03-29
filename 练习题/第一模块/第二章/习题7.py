#! -*- coding:utf-8 -*-
dic={'k1':'v1','k2':'v2','k3':[11,22,33]}
for i in dic.keys():
    print(i)
for i in dic.values():
    print(i)
for i,j in dic.items() :
    print(i,j)
dic.setdefault('k4','v4')
print(dic)
dic['k1']='alex'
print(dic)
dic['k3'].append(44)
print(dic)
dic['k3'].insert(0,18)
print(dic)