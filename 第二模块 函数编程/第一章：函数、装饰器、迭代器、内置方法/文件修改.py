# 文件修改（占硬盘方式）

import os
f_old=open(r'C:\Users\夏天\Desktop\prtice.txt',mode='r+',encoding='utf-8')
# f_new=open(r'C:\Users\夏天\Desktop\prtice.txt.new',mode='w',encoding= 'utf-8')
for lin in f_old:
    if '以前' in lin:
        lin=lin.replace('以前','增加')  #将文件中为‘玉玉’的字符修改成‘何芳华’
    # f_new.write(lin)

f_old.close()
# f_new.close()
# os.remove(r'C:\Users\夏天\Desktop\prtice.txt')
# os.rename(r'C:\Users\夏天\Desktop\prtice.txt.new',r'C:\Users\夏天\Desktop\prtice.txt')


# 文件修改（占内存方式）
# f=open(r'C:\Users\夏天\Desktop\prtice.txt',mode='r+',encoding='utf-8')
# a=f.read()
#
# if '增加' in a:
#     b=a.replace('增加','何芳华')
# f.seek(0)                              #将光标移动到文件开头，使下一步写文件时从文件开头开始写，将原文件覆盖
# f.write(b)
# f.close()

