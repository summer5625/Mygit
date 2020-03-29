#普通条件语句
# a=1
# b=2
# # if a<b:
# #     c=a
# # else:
# #     c=b
# # print(c)3
# #三元运算
#
# c=a if a<b else b
# print(c)

#文件操作：读文件
# f=open(file='练习.txt',mode='r',encoding='UTF-8')
# data=f.read()
# print(data)
# f.close()

#文件操作：二进制读文件
# f=open(r'C:\Users\夏天\Desktop\新建文本文档.txt',mode='r',encoding='GBK')
# data=f.read()
# print(data)
# f.close()

# import
# chardet
# f = open(r'C:\Users\夏天\Desktop\新建文本文档.txt', mode='rb')
# data = f.read()
# print(data)
# f.close()
# a = chardet.detect(data)
# print(a)
# b = data.decode('ISO-8859-1')

#文件操作：文件处理
# f=open('练习.txt',mode='r',encoding='utf-8')
# a=f.read()
# # for line in f:
# #     print(line)
# print(a)
# f.close()

#文件操作：文件写

f=open('练习.txt',mode='w',encoding='utf-8')
f.write('玉玉  那你  56\n')
f.write('玉玉  爱你  86\n')
f.write('何芳华  love 996\n')
f.write('i love 何芳华!')
f.close()

#文件操作：文件写(二进制写）
# f=open('练习3.txt',mode='wb')
# f.write('i love 何芳华' )
# f.close()

#文件操作：文件写(追加）
# f=open('练习.txt',mode='ab')
# f.write('\ni love 何芳华!'.encode()  )
# f.close()


#文件操作：文件读写模式（先读在写）
# f=open('练习4.txt',mode='r+',encoding= 'utf-8')
# a=f.read()
# print('old',a)
# f.write('\nlove you')
# f.write('\nlove you forever')
# b=f.read()
# print('new',b)


#文件操作：文件读写模式（先写在读）
# f=open('练习4.txt',mode='w+',encoding= 'utf-8')
# a=f.read()
# print('old',a)
# f.write('\nlove you')
# f.write('\nlove you forever')
# b=f.read()
# print('new',b)
