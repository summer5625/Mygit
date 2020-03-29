# import sys
# print(sys.maxsize)
# print(sys.platform)
# print(sys.stdout)
# print(sys.stdout.write('hh'))

# import shutil

# f1 = open('OS模块.py','r',encoding='utf-8')
# f2 = open('OS模块_new.py','w',encoding='utf-8')
#
# shutil.copyfileobj(f1,f2)
#
# shutil.copytree('crm','crm2')   #拷贝文件夹
#
# shutil.copytree('crm','crm3',ignore=shutil.ignore_patterns('__init__.py','saybey.py'))  #复制时指定文件不复制


#压缩文件
# ret = shutil.make_archive(r'C:\Users\夏天\Desktop','zip',r'C:\Users\夏天\Desktop\python学习')
# print(ret)



# import zipfile
#压缩
# z = zipfile.ZipFile(r'C:\Users\夏天\Desktop\python.zip','w')   #压缩后的文件名称中不能出现中文
# z.write(r'C:\Users\夏天\Desktop\python学习\PyCharm 使用技巧.docx')
# z.write(r'C:\Users\夏天\Desktop\python学习')
# z.close()

#解压
# z = zipfile.ZipFile(r'C:\Users\夏天\Desktop\python.zip', 'r')
# z.extractall(path=r'C:\Users\夏天\Desktop\python')
# z.close()


import tarfile

t = tarfile.open(r'C:\Users\夏天\Desktop\python.zip','w')
t.add(r'C:\Users\夏天\Desktop\python学习',arcname='python学习')
t.close()