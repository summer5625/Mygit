import shelve
data = {'k1':123,'k2':'Hello'}
lis = [1,2,3,'abc']

# f = shelve.open(r'C:\Users\夏天\Desktop\py123')  #
# f['data'] = data
# f['lis'] = lis
# f.close()


d = shelve.open(r'C:\Users\夏天\Desktop\py123')
# #
# print(d['data'])
# print(d['lis'])
#
#
# del  d['lis']  #删除
# d.close()

# c = shelve.open(r'C:\Users\夏天\Desktop\py123')
#
# print(c['lis'])  #如果没有lis则会报错


# d['lis'] = [1,'oo',3,'abc']   #修改数据，不能以d['lis'][1]='oo'方式修改
# f.close()

a = shelve.open(r'C:\Users\夏天\Desktop\py123')
# print(a['lis'])

