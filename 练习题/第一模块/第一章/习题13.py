#使用while,完成以下图形的输出图像
n=9
a="*  "
while n>0:
    if n>4:
     print(a*(10-n))
    else:
      print(a*n)
    n-=1

