#json模块

# import json
# data = {'k1':123,'k2':'Hello'}
# lis = [1,2,3,'abc']
#
# a = json.dumps(data)   #dumps仅将数据类型转换成字符串
# print(a)
# print(type(a))
#
# b = json.loads(a)   #仅将字符串转换成数据类型
# print(b)
# print(type(b))
#
# f = open(r'C:\Users\夏天\Desktop\prtic.json','w',encoding='utf-8')   #将文件类型转换成字符串并存入指定的文件中
# json.dump(data,f)
# json.dump(lis,f)
# f2 = open(r'C:\Users\夏天\Desktop\prtic.json','r',encoding='utf-8')   #将文件的内容转换成相应的数据类型
# x = json.load(f2)
# print(x)
# print(type(x))



#pickle模块

import pickle
#
data = {'k1':123,'k2':'Hello'}
lis = [1,2,3,'abc']

# pk = pickle.dumps(data)  #将数据类型转成bytes类型
# print(pk)
# print(type(pk))
#
# f = open(r'C:\Users\夏天\Desktop\prtic.pkl','wb')
# pickle.dump(lis,f)
# f.close()
#
#
f2 = open(r'C:\Users\夏天\Desktop\prtic.pkl','rb')
x = pickle.load(f2)
print(type(x))
